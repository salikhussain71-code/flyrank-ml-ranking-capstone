from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.ranking import baseline_score, precision_at_k, recall_at_k, reciprocal_rank, ndcg_at_k

DATA = ROOT / "data" / "demo_queries.csv"
OUT = ROOT / "outputs"

def main():
    df = pd.read_csv(DATA).fillna("")
    df["score"] = df.apply(lambda r: baseline_score(r["query"], r["title"], r["snippet"]), axis=1)
    ranked = df.sort_values(["query_id", "score", "document_id"], ascending=[True, False, True]).copy()
    ranked["rank"] = ranked.groupby("query_id").cumcount() + 1
    OUT.mkdir(exist_ok=True)
    ranked.to_csv(OUT / "ranked_demo_results.csv", index=False)
    rows=[]
    for qid, group in ranked.groupby("query_id", sort=True):
        rels = group.sort_values("rank")["relevance"].astype(int).tolist()
        total = sum(1 for r in rels if r > 0)
        rows.append({"query_id": qid, "n_documents": len(rels), "relevant_documents": total,
                     "P@3": round(precision_at_k(rels, 3), 4),
                     "R@3": round(recall_at_k(rels, total, 3), 4),
                     "MRR": round(reciprocal_rank(rels), 4),
                     "NDCG@3": round(ndcg_at_k(rels, 3), 4)})
    metrics = pd.DataFrame(rows)
    metrics.to_csv(OUT / "demo_metrics_by_query.csv", index=False)
    print("DEMO DATA ONLY — do not present these values as real search performance.")
    print(metrics.to_string(index=False))
    print(f"\nSaved: {OUT / 'ranked_demo_results.csv'}")
    print(f"Saved: {OUT / 'demo_metrics_by_query.csv'}")

if __name__ == "__main__":
    main()
