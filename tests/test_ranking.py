import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.ranking import baseline_score, precision_at_k, recall_at_k, reciprocal_rank, ndcg_at_k

class RankingTests(unittest.TestCase):
    def test_title_match_scores_higher_than_unrelated_page(self):
        self.assertGreater(baseline_score("python machine learning", "Python Machine Learning", "tools"),
                           baseline_score("python machine learning", "Campus Dining", "menu hours"))
    def test_precision_at_k(self):
        self.assertAlmostEqual(precision_at_k([1, 0, 1], 3), 2/3)
    def test_recall_at_k(self):
        self.assertAlmostEqual(recall_at_k([1, 0, 1], 2, 3), 1.0)
    def test_mrr(self):
        self.assertAlmostEqual(reciprocal_rank([0, 1, 0]), 0.5)
    def test_ndcg_perfect_order(self):
        self.assertAlmostEqual(ndcg_at_k([1, 1, 0], 3), 1.0)
    def test_invalid_k(self):
        with self.assertRaises(ValueError): precision_at_k([1], 0)

if __name__ == "__main__":
    unittest.main()
