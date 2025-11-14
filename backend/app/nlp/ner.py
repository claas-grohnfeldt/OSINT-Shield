from __future__ import annotations

import re
from dataclasses import dataclass

import spacy
from spacy.language import Language
from spacy.pipeline import EntityRuler

from ..models.entity import EntityType


@dataclass(slots=True)
class ExtractedEntity:
    entity_type: EntityType
    value: str
    confidence: float = 0.6


class ThreatNER:
    """Hybrid rule-based extractor focused on cyber/hybrid threat indicators."""

    def __init__(self) -> None:
        self.nlp: Language = spacy.blank("en")
        ruler = self.nlp.add_pipe("entity_ruler")
        ruler.add_patterns(_entity_patterns())
        self._regex_rules = [
            (re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), EntityType.IP, 0.9),
            (
                re.compile(r"\b[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+\b"),
                EntityType.DOMAIN,
                0.75,
            ),
            (
                re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE),
                EntityType.CVE,
                0.95,
            ),
            (
                re.compile(r"\b(?:[A-Fa-f0-9]{64}|[A-Fa-f0-9]{40})\b"),
                EntityType.HASH,
                0.85,
            ),
        ]

    def extract(self, text: str) -> list[ExtractedEntity]:
        doc = self.nlp(text)
        entities: list[ExtractedEntity] = []
        seen: set[tuple[EntityType, str]] = set()

        for ent in doc.ents:
            entity_type = _map_label(ent.label_)
            key = (entity_type, ent.text.lower())
            if entity_type and key not in seen:
                entities.append(ExtractedEntity(entity_type=entity_type, value=ent.text, confidence=0.65))
                seen.add(key)

        for regex, entity_type, confidence in self._regex_rules:
            for match in regex.findall(text):
                key = (entity_type, match.lower())
                if key in seen:
                    continue
                entities.append(ExtractedEntity(entity_type=entity_type, value=match, confidence=confidence))
                seen.add(key)

        return entities


def _entity_patterns() -> list[dict]:
    return [
        {"label": "ORG", "pattern": "Gazprom"},
        {"label": "ORG", "pattern": "Europol"},
        {"label": "THREAT", "pattern": "Killnet"},
        {"label": "THREAT", "pattern": "Sandworm"},
        {"label": "GPE", "pattern": "Ukraine"},
        {"label": "GPE", "pattern": "Poland"},
        {"label": "GPE", "pattern": "Germany"},
        {"label": "FACILITY", "pattern": "LNG terminal"},
        {"label": "FACILITY", "pattern": "substation"},
    ]


def _map_label(label: str) -> EntityType:
    mapping = {
        "ORG": EntityType.ORG,
        "GPE": EntityType.COUNTRY,
        "LOC": EntityType.CITY,
        "FACILITY": EntityType.FACILITY,
        "PERSON": EntityType.PERSON,
        "THREAT": EntityType.THREAT_ACTOR,
    }
    return mapping.get(label, EntityType.UNKNOWN)


__all__ = ["ThreatNER", "ExtractedEntity"]
