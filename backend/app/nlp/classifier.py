from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


@dataclass(slots=True)
class RelevanceResult:
    is_relevant: bool
    score: float


class RelevanceClassifier:
    """Tiny TF-IDF + Logistic Regression classifier for security relevance."""

    def __init__(self) -> None:
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, stop_words="english")
        self.model = LogisticRegression(max_iter=400)
        texts, labels = self._training_corpus()
        matrix = self.vectorizer.fit_transform(texts)
        self.model.fit(matrix, labels)

    def predict_score(self, text: str) -> float:
        probs = self.model.predict_proba(self.vectorizer.transform([text]))
        return float(probs[0][1])

    def get_relevance(self, text: str, threshold: float = 0.55) -> RelevanceResult:
        score = self.predict_score(text)
        return RelevanceResult(is_relevant=score >= threshold, score=score)

    @staticmethod
    def _training_corpus() -> tuple[list[str], list[int]]:
        relevant_samples = [
            "russian threat actor targets polish energy grid",
            "coordinated drone disruption reported near german port",
            "ransomware hits satellite operator impacting european flights",
            "ddos against estonian government services claimed by killnet",
            "critical infrastructure malware telemetry indicates lateral movement",
        ]
        benign_samples = [
            "local sports club celebrates championship",
            "weather remains sunny across southern france",
            "european film festival announces nominees",
            "community garden initiative expands",
            "tourism board promotes alpine hiking",
        ]
        return relevant_samples + benign_samples, [1] * len(relevant_samples) + [0] * len(benign_samples)


__all__ = ["RelevanceClassifier", "RelevanceResult"]
