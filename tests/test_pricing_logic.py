import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.pricing_pipeline import recommend_price


def test_recommend_price_returns_better_revenue():
    result = recommend_price(
        base_price=120.0,
        competitor_price=110.0,
        inventory_level=80,
        category="Electronics",
        is_weekend=0,
        month=7,
        is_promotion=1,
        current_price=118.0,
    )

    assert result["recommended_price"] > 0
    assert result["predicted_demand"] > 0
    assert result["predicted_revenue"] >= result["current_revenue"]
    assert result["pricing_signal"] in {"underpriced", "fair", "overpriced"}
