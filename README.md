# Supply Chain Analytics

A Streamlit inventory-planning demo built around generated SKU demand, stock-on-hand, lead-time, and unit-cost data.

## Dashboard features

- Generates a reproducible sample of 350 SKUs across four categories.
- Estimates a reorder point from daily demand and lead time, with a variability buffer.
- Labels items as **Reorder**, **Healthy**, or **Overstock**.
- Filters by category and visualizes stock status and demand versus inventory.
- Exports an enriched replenishment table with suggested order quantities.

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Scope

All default inventory and demand values are synthetic. The reorder formula is a demonstration and does not account for supplier constraints, service-level policy, seasonality, pack sizes, or actual purchase orders. Validate assumptions before operational use.

## Maintainer

Ravi Kumar Rao · [GitHub](https://github.com/Ravi506051)
