import polars as pl
from collections import Counter

df = pl.read_csv("2024_fb_ads_president_scored_anon.csv")
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

numeric_dtypes = [pl.Int64, pl.Float64, pl.Int32, pl.Float32]
numeric_cols = [col for col in df.columns if df.schema[col] in numeric_dtypes]

# Global Stats
print("Global Descriptive Statistics:\n")
for col in df.columns:
    dtype = df.schema[col]
    series = df[col].drop_nulls()
    count = series.len()
    print(f" {col} ({'numeric' if dtype in numeric_dtypes else 'string'}):")
    if dtype in numeric_dtypes:
        print(f"  count: {count}, mean: {series.mean():.2f}, min: {series.min():.2f}, max: {series.max():.2f}, std_dev: {series.std():.2f}\n")
    else:
        vals = series.to_list()
        common = Counter(vals).most_common(1)
        print(f"  count: {count}, unique_values: {len(set(vals))}, most_common: {common[0] if common else None}\n")

# Group by page_id
print("Grouped by page_id (First 3):\n")
grouped1 = df.group_by("page_id").agg(
    [pl.col(c).count().alias(f"{c}_count") for c in numeric_cols] +
    [pl.col(c).mean().alias(f"{c}_mean") for c in numeric_cols] +
    [pl.col(c).min().alias(f"{c}_min") for c in numeric_cols] +
    [pl.col(c).max().alias(f"{c}_max") for c in numeric_cols] +
    [pl.col(c).std().alias(f"{c}_std_dev") for c in numeric_cols]
)

for row in grouped1.head(3).iter_rows(named=True):
    print(f"=== page_id: {row['page_id']} ===")
    for col in numeric_cols:
        print(f"{col:<45} | {{'count': {row[f'{col}_count']}, 'mean': {row[f'{col}_mean']:.2f}, 'min': {row[f'{col}_min']:.2f}, 'max': {row[f'{col}_max']:.2f}, 'std_dev': {0.0 if row[f'{col}_std_dev'] is None else round(row[f'{col}_std_dev'], 2)}}}")

# Group by (page_id, ad_id)
print("\nGrouped by (page_id, ad_id) (First 3):\n")
grouped2 = df.group_by(["page_id", "ad_id"]).agg(
    [pl.col(c).count().alias(f"{c}_count") for c in numeric_cols] +
    [pl.col(c).mean().alias(f"{c}_mean") for c in numeric_cols] +
    [pl.col(c).min().alias(f"{c}_min") for c in numeric_cols] +
    [pl.col(c).max().alias(f"{c}_max") for c in numeric_cols] +
    [pl.col(c).std().alias(f"{c}_std_dev") for c in numeric_cols]
)

for row in grouped2.head(3).iter_rows(named=True):
    print(f"=== page_id: {row['page_id']}, ad_id: {row['ad_id']} ===")
    for col in numeric_cols:
        print(f"{col:<45} | {{'count': {row[f'{col}_count']}, 'mean': {row[f'{col}_mean']:.2f}, 'min': {row[f'{col}_min']:.2f}, 'max': {row[f'{col}_max']:.2f}, 'std_dev': {0.0 if row[f'{col}_std_dev'] is None else round(row[f'{col}_std_dev'], 2)}}}")
