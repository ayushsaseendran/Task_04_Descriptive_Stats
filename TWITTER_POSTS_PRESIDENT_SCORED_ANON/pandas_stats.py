import pandas as pd
import numpy as np

df = pd.read_csv('2024_tw_posts_president_scored_anon.csv')

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

print(" Global Descriptive Statistics:\n")
for col in df.columns:
    if col in numeric_cols:
        stats = df[col].describe()
        print(f"{col:<45} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {df[col].std():.2f}}}")
    else:
        top = df[col].value_counts(dropna=True).head(1)
        val, freq = (top.index[0], top.iloc[0]) if not top.empty else ("N/A", 0)
        print(f"{col:<45} | {{'count': {df[col].count()}, 'unique': {df[col].nunique()}, 'most_common': ('{val}', {freq})}}")

# Group by 'id'
print("\n Grouped by id (First 3 Groups):\n")
grouped = df.groupby('id')[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
for idx, (id_, data) in enumerate(grouped.iterrows()):
    if idx >= 3: break
    print(f"=== id: {id_} ===")
    for col in numeric_cols:
        stats = data[col]
        print(f"{col:<45} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {0.0 if pd.isna(stats['std']) else round(stats['std'], 2)}}}")
    print()

# Group by ('id', 'url')
print("\n Grouped by (id, url) (First 3 Groups):\n")
grouped = df.groupby(['id', 'url'])[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
for idx, (group_key, data) in enumerate(grouped.iterrows()):
    if idx >= 3: break
    print(f"=== id: {group_key[0]}, url: {group_key[1]} ===")
    for col in numeric_cols:
        stats = data[col]
        print(f"{col:<45} | {{'count': {int(stats['count'])}, 'mean': {stats['mean']:.2f}, 'min': {stats['min']:.2f}, 'max': {stats['max']:.2f}, 'std_dev': {0.0 if pd.isna(stats['std']) else round(stats['std'], 2)}}}")
    print()
