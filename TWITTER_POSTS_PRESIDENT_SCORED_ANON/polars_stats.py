import polars as pl
from collections import Counter

# Load the dataset
df = pl.read_csv("2024_tw_posts_president_scored_anon.csv")
print(f" Loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

# Classify columns
numeric_dtypes = [pl.Int64, pl.Float64, pl.Int32, pl.Float32]
numeric_cols = [col for col in df.columns if df.schema[col] in numeric_dtypes]
non_numeric_cols = [col for col in df.columns if df.schema[col] not in numeric_dtypes]

# Global Descriptive Statistics
print(" Global Descriptive Statistics:\n")
for col in df.columns:
    dtype = df.schema[col]
    col_series = df[col].drop_nulls()
    count = col_series.len()

    if dtype in numeric_dtypes:
        mean = col_series.mean()
        min_ = col_series.min()
        max_ = col_series.max()
        std = col_series.std()
        print(f"{col:<45} | {{'count': {count}, 'mean': {mean:.2f}, 'min': {min_:.2f}, 'max': {max_:.2f}, 'std_dev': {0.0 if std is None else round(std, 2)}}}")
    else:
        unique = col_series.n_unique()
        most_common = Counter(col_series).most_common(1)[0] if count > 0 else ("N/A", 0)
        print(f"{col:<45} | {{'count': {count}, 'unique': {unique}, 'most_common': {most_common}}}")

print("\n Grouped by ('id',) (First 3 Groups):\n")
keys = ["id"]
grouped = df.group_by(keys).agg(
    [pl.col(col).count().alias(f"{col}_count") for col in numeric_cols] +
    [pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols] +
    [pl.col(col).min().alias(f"{col}_min") for col in numeric_cols] +
    [pl.col(col).max().alias(f"{col}_max") for col in numeric_cols] +
    [pl.col(col).std().alias(f"{col}_std_dev") for col in numeric_cols]
)

for row in grouped.head(3).iter_rows(named=True):
    header = ", ".join([f"{k}: {row[k]}" for k in keys])
    print(f"=== {header} ===")
    for col in numeric_cols:
        count = row.get(f"{col}_count")
        mean = row.get(f"{col}_mean")
        min_ = row.get(f"{col}_min")
        max_ = row.get(f"{col}_max")
        std = row.get(f"{col}_std_dev")

        mean_str = f"{mean:.2f}" if mean is not None else "NA"
        min_str = f"{min_:.2f}" if min_ is not None else "NA"
        max_str = f"{max_:.2f}" if max_ is not None else "NA"
        std_str = f"{round(std, 2)}" if std is not None else "0.0"

        print(f"{col:<45} | {{'count': {count}, 'mean': {mean_str}, 'min': {min_str}, 'max': {max_str}, 'std_dev': {std_str}}}")
    print()

print("\n Grouped by ('id', 'url') (First 3 Groups):\n")
keys = ["id", "url"]
grouped = df.group_by(keys).agg(
    [pl.col(col).count().alias(f"{col}_count") for col in numeric_cols] +
    [pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols] +
    [pl.col(col).min().alias(f"{col}_min") for col in numeric_cols] +
    [pl.col(col).max().alias(f"{col}_max") for col in numeric_cols] +
    [pl.col(col).std().alias(f"{col}_std_dev") for col in numeric_cols]
)

for row in grouped.head(3).iter_rows(named=True):
    header = ", ".join([f"{k}: {row[k]}" for k in keys])
    print(f"=== {header} ===")
    for col in numeric_cols:
        count = row.get(f"{col}_count")
        mean = row.get(f"{col}_mean")
        min_ = row.get(f"{col}_min")
        max_ = row.get(f"{col}_max")
        std = row.get(f"{col}_std_dev")

        mean_str = f"{mean:.2f}" if mean is not None else "NA"
        min_str = f"{min_:.2f}" if min_ is not None else "NA"
        max_str = f"{max_:.2f}" if max_ is not None else "NA"
        std_str = f"{round(std, 2)}" if std is not None else "0.0"

        print(f"{col:<45} | {{'count': {count}, 'mean': {mean_str}, 'min': {min_str}, 'max': {max_str}, 'std_dev': {std_str}}}")
    print()
