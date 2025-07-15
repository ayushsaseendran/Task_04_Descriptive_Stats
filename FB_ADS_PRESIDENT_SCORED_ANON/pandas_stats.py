import pandas as pd
import numpy as np

df = pd.read_csv("2024_fb_ads_president_scored_anon.csv")
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
non_numeric_cols = df.select_dtypes(exclude=np.number).columns.tolist()

# Global Stats
print(" Global Descriptive Statistics:\n")
for col in non_numeric_cols:
    print(f"{col} (string):")
    print(f"  count: {df[col].count()}")
    print(f"  unique_values: {df[col].nunique()}")
    common = df[col].value_counts().head(1)
    print(f"  most_common: {common.index[0], common.iloc[0] if not common.empty else 'None'}\n")

for col in numeric_cols:
    stats = df[col].describe()
    print(f"{col} (numeric):")
    print(f"  count: {int(stats['count'])}, mean: {stats['mean']:.2f}, min: {stats['min']:.2f}, max: {stats['max']:.2f}, std_dev: {df[col].std():.2f}\n")

# Group by page_id
print("Grouped by page_id (First 3):\n")
g1 = df.groupby("page_id")[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
for idx, (gid, stats) in enumerate(g1.iterrows()):
    if idx >= 3: break
    print(f"=== page_id: {gid} ===")
    for col in numeric_cols:
        vals = stats[col]
        print(f"{col:<45} | {{'count': {int(vals['count'])}, 'mean': {vals['mean']:.2f}, 'min': {vals['min']:.2f}, 'max': {vals['max']:.2f}, 'std_dev': {0.0 if pd.isna(vals['std']) else round(vals['std'], 2)}}}")

# Group by (page_id, ad_id)
print("\n Grouped by (page_id, ad_id) (First 3):\n")
g2 = df.groupby(["page_id", "ad_id"])[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
for idx, (gid, stats) in enumerate(g2.iterrows()):
    if idx >= 3: break
    pid, aid = gid
    print(f"=== page_id: {pid}, ad_id: {aid} ===")
    for col in numeric_cols:
        vals = stats[col]
        print(f"{col:<45} | {{'count': {int(vals['count'])}, 'mean': {vals['mean']:.2f}, 'min': {vals['min']:.2f}, 'max': {vals['max']:.2f}, 'std_dev': {0.0 if pd.isna(vals['std']) else round(vals['std'], 2)}}}")

