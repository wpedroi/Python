import pandas as pd

# 1. Read CSV files
store_df = pd.read_csv("Qty_shop.csv", dtype=str)
stock_df = pd.read_csv("Qty_stored.csv", dtype=str)

# 2. Merge stock quantity based on SKU
merged = pd.merge(
    store_df,
    stock_df[["sku", "qty"]],
    on="sku",
    how="left",
    suffixes=("", "_stock"),
)

# 3. Copy quantity to 'qtynew'
store_df["qtynew"] = merged["qty_stock"].fillna(0)

# 4. Save updated file
store_df.to_csv("الكميات_في_المتجر_المحدثة.csv", index=False, encoding="utf-8-sig")