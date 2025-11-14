from __future__ import annotations

from collections import defaultdict

from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer

from ..models.event import Event


def cluster_events(events: list[Event], max_clusters: int = 3) -> dict[str, list[Event]]:
    """Group events by text similarity; returns mapping cluster_id -> events."""

    if not events:
        return {}
    if len(events) <= 2:
        return {"cluster_0": events}

    texts = [event.text for event in events]
    vectorizer = TfidfVectorizer(max_features=500, stop_words="english")
    matrix = vectorizer.fit_transform(texts).toarray()
    n_clusters = min(max_clusters, len(events))
    clustering = AgglomerativeClustering(n_clusters=n_clusters)
    labels = clustering.fit_predict(matrix)

    grouped: dict[str, list[Event]] = defaultdict(list)
    for label, event in zip(labels, events, strict=False):
        grouped[f"cluster_{label}"].append(event)
    return grouped


__all__ = ["cluster_events"]
