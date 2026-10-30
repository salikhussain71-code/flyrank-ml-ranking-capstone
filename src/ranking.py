"""Simple, explainable baseline ranking and information-retrieval metrics."""
from __future__ import annotations
import math
import re
from collections import Counter

STOPWORDS = {"a", "an", "and", "are", "for", "how", "in", "of", "the", "to", "with", "what"}
TOKEN_RE = re.compile(r"[a-z0-9]+", re.I)

def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(str(text)) if t.lower() not in STOPWORDS]

def baseline_score(query: str, title: str, snippet: str) -> float:
    """Score a page using query-token overlap; title matches receive extra weight."""
    q = set(tokenize(query))
    if not q:
        return 0.0
    title_tokens = tokenize(title)
    snippet_tokens = tokenize(snippet)
    title_counts = Counter(title_tokens)
    snippet_counts = Counter(snippet_tokens)
    return sum(2.0 * title_counts[t] + 0.5 * snippet_counts[t] for t in q) / len(q)

def precision_at_k(relevances: list[int], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    return sum(1 if r > 0 else 0 for r in relevances[:k]) / k

def recall_at_k(relevances: list[int], total_relevant: int, k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if total_relevant <= 0:
        return 0.0
    return sum(1 if r > 0 else 0 for r in relevances[:k]) / total_relevant

def reciprocal_rank(relevances: list[int]) -> float:
    for rank, rel in enumerate(relevances, start=1):
        if rel > 0:
            return 1.0 / rank
    return 0.0

def ndcg_at_k(relevances: list[int], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    gains = [float(2**int(r) - 1) for r in relevances[:k]]
    dcg = sum(g / math.log2(i + 2) for i, g in enumerate(gains))
    ideal = sorted((float(2**int(r) - 1) for r in relevances), reverse=True)[:k]
    idcg = sum(g / math.log2(i + 2) for i, g in enumerate(ideal))
    return dcg / idcg if idcg else 0.0
