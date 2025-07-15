import polars as pl
from collections import Counter

# Load the dataset
df = pl.read_csv('../FB_POSTS_PRESIDENT_SCORED_ANON/2024_fb_posts_president_scored_anon.csv')
print(f" Loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

# Identify numeric columns
numeric_dtypes = [pl.Int64, pl.Float64, pl.Int32, pl.Float32]
numeric_cols = [col for col in df.columns if df.schema[col] in numeric_dtypes]

# 🔹 Global Descriptive Stats
print(" Global Descriptive Statistics:\n")
for col in df.columns:
    dtype = df.schema[col]
    print(f" {col} ({'numeric' if dtype in numeric_dtypes else 'string'}):")
    try:
        col_series = df[col].drop_nulls()
        count = col_series.len()
        if dtype in numeric_dtypes:
            mean = col_series.mean()
            min_ = col_series.min()
            max_ = col_series.max()
            std = col_series.std()
            print(f"  count: {count}")
            print(f"  mean: {mean:.2f}")
            print(f"  min: {min_:.2f}")
            print(f"  max: {max_:.2f}")
            print(f"  std_dev: {std:.2f}\n")
        else:
            unique = col_series.n_unique()
            most_common = Counter(col_series).most_common(1)[0] if count > 0 else ("N/A", 0)
            print(f"  count: {count}")
            print(f"  unique_values: {unique}")
            print(f"  most_common: {most_common}\n")
    except Exception as e:
        print(f"  Could not compute stats: {e}\n")

# --------------------------------------------
# Aggregation 1: By Facebook_Id
# --------------------------------------------
print(" Grouped Statistics by Facebook_Id (First 3 Groups):\n")
grouped = df.group_by("Facebook_Id").agg(
    [pl.col(col).count().alias(f"{col}_count") for col in numeric_cols] +
    [pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols] +
    [pl.col(col).min().alias(f"{col}_min") for col in numeric_cols] +
    [pl.col(col).max().alias(f"{col}_max") for col in numeric_cols] +
    [pl.col(col).std().fill_nan(0.0).alias(f"{col}_std_dev") for col in numeric_cols]
)

for row in grouped.head(3).iter_rows(named=True):
    print(f"=== Facebook_Id: {row['Facebook_Id']} ===")
    for col in numeric_cols:
        stats = {
            "count": row[f"{col}_count"],
            "mean": row[f"{col}_mean"],
            "min": row[f"{col}_min"],
            "max": row[f"{col}_max"],
            "std_dev": row[f"{col}_std_dev"],
        }
        print(f"{col:<50} | {stats}")
    print()

# --------------------------------------------
#  Aggregation 2: By Facebook_Id + post_id
# --------------------------------------------
print(" Grouped Statistics by Facebook_Id + post_id (First 3 Groups):\n")
grouped = df.group_by(["Facebook_Id", "post_id"]).agg(
    [pl.col(col).count().alias(f"{col}_count") for col in numeric_cols] +
    [pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols] +
    [pl.col(col).min().alias(f"{col}_min") for col in numeric_cols] +
    [pl.col(col).max().alias(f"{col}_max") for col in numeric_cols] +
    [pl.col(col).std().fill_nan(0.0).alias(f"{col}_std_dev") for col in numeric_cols]
)

for row in grouped.head(3).iter_rows(named=True):
    print(f"=== Facebook_Id: {row['Facebook_Id']}, post_id: {row['post_id']} ===")
    for col in numeric_cols:
        stats = {
            "count": row[f"{col}_count"],
            "mean": row[f"{col}_mean"],
            "min": row[f"{col}_min"],
            "max": row[f"{col}_max"],
            "std_dev": row[f"{col}_std_dev"],
        }
        print(f"{col:<50} | {stats}")
    print()

# --------------------------------------------
# Aggregation 3: By Page Category + post_id
# --------------------------------------------
print(" Grouped Statistics by Page Category + post_id (First 3 Groups):\n")
if "Page Category" in df.columns:
    grouped = df.group_by(["Page Category", "post_id"]).agg(
        [pl.col(col).count().alias(f"{col}_count") for col in numeric_cols] +
        [pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols] +
        [pl.col(col).min().alias(f"{col}_min") for col in numeric_cols] +
        [pl.col(col).max().alias(f"{col}_max") for col in numeric_cols] +
        [pl.col(col).std().fill_nan(0.0).alias(f"{col}_std_dev") for col in numeric_cols]
    )

    for row in grouped.head(3).iter_rows(named=True):
        print(f"=== Page Category: {row['Page Category']}, post_id: {row['post_id']} ===")
        for col in numeric_cols:
            stats = {
                "count": row[f"{col}_count"],
                "mean": row[f"{col}_mean"],
                "min": row[f"{col}_min"],
                "max": row[f"{col}_max"],
                "std_dev": row[f"{col}_std_dev"],
            }
            print(f"{col:<50} | {stats}")
        print()
else:
    print(" 'Page Category' column not found. Skipping this group.\n")
