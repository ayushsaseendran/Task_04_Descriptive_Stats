import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('../FB_POSTS_PRESIDENT_SCORED_ANON/2024_fb_posts_president_scored_anon.csv')

# Identify numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

print(f" Loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

# ----------------------------------------
# Global Descriptive Statistics
# ----------------------------------------

print(" Global Descriptive Statistics:\n")

# Non-numeric fields
for col in non_numeric_cols:
    print(f" {col} (string):")
    print(f"  count: {df[col].count()}")
    print(f"  unique_values: {df[col].nunique()}")
    most_common = df[col].value_counts().head(1)
    if not most_common.empty:
        val, freq = most_common.index[0], most_common.iloc[0]
        print(f"  most_common: ('{val}', {freq})")
    else:
        print("  most_common: None")
    print()

# Numeric fields
for col in numeric_cols:
    stats = df[col].describe()
    std = df[col].std()
    print(f" {col} (numeric):")
    print(f"  count: {int(stats['count'])}")
    print(f"  mean: {stats['mean']:.2f}")
    print(f"  min: {stats['min']:.2f}")
    print(f"  max: {stats['max']:.2f}")
    print(f"  std_dev: {std:.2f}")
    print()

# ----------------------------------------
# Grouped Statistics by Facebook_Id
# ----------------------------------------

print(" Grouped Statistics by Facebook_Id (First 3 Groups):\n")
grouped_facebook = df.groupby("Facebook_Id")[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])

for idx, (group, data) in enumerate(grouped_facebook.iterrows()):
    if idx >= 3:
        break
    print(f"=== Facebook_Id: {group} ===")
    for col in numeric_cols:
        stats = data[col]
        print(f"{col:<50} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {0.0 if pd.isna(stats['std']) else round(stats['std'], 2)}}}")
    print()

# ----------------------------------------
# Grouped Statistics by Facebook_Id + post_id
# ----------------------------------------

print(" Grouped Statistics by Facebook_Id + post_id (First 3 Groups):\n")
grouped_both = df.groupby(["Facebook_Id", "post_id"])[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])

for idx, (group, data) in enumerate(grouped_both.iterrows()):
    if idx >= 3:
        break
    facebook_id, post_id = group
    print(f"=== Facebook_Id: {facebook_id}, post_id: {post_id} ===")
    for col in numeric_cols:
        stats = data[col]
        print(f"{col:<50} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {0.0 if pd.isna(stats['std']) else round(stats['std'], 2)}}}")
    print()

# ----------------------------------------
#  Grouped Statistics by Page Category + post_id
# ----------------------------------------

if "Page Category" in df.columns:
    print(" Grouped Statistics by Page Category + post_id (First 3 Groups):\n")
    grouped_extra = df.groupby(["Page Category", "post_id"])[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])

    for idx, (group, data) in enumerate(grouped_extra.iterrows()):
        if idx >= 3:
            break
        page_cat, post_id = group
        print(f"=== Page Category: {page_cat}, post_id: {post_id} ===")
        for col in numeric_cols:
            stats = data[col]
            print(f"{col:<50} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {0.0 if pd.isna(stats['std']) else round(stats['std'], 2)}}}")
        print()
else:
    print(" 'Page Category' column not found. Skipping third grouping.")
