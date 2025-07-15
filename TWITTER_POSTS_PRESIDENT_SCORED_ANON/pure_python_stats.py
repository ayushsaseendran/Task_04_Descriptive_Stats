import csv
import math
from collections import defaultdict, Counter

def clean_val(val):
    return val if val not in ("", "null", "None", "NA", "N/A") else None

def is_number(val):
    try:
        float(val)
        return True
    except:
        return False

def compute_numeric_stats(values):
    numeric_vals = [float(v) for v in values if is_number(v)]
    if not numeric_vals:
        return None
    count = len(numeric_vals)
    mean = sum(numeric_vals) / count
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric_vals) / count)
    return {
        'count': count,
        'mean': round(mean, 2),
        'min': round(min(numeric_vals), 2),
        'max': round(max(numeric_vals), 2),
        'std_dev': round(std_dev, 2)
    }

def compute_string_stats(values):
    values = [v for v in values if v is not None]
    freq = Counter(values)
    return {
        'count': len(values),
        'unique': len(set(values)),
        'most_common': freq.most_common(1)[0] if freq else None
    }

file_path = '2024_tw_posts_president_scored_anon.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    columns = reader.fieldnames

column_types = {}
for col in columns:
    sample = [clean_val(row[col]) for row in rows if clean_val(row[col]) is not None][:100]
    column_types[col] = 'numeric' if all(is_number(v) for v in sample) else 'string'

cleaned_data = defaultdict(list)
for col in columns:
    for row in rows:
        raw_val = clean_val(row[col])
        if raw_val is None:
            raw_val = '0.0' if column_types[col] == 'numeric' else 'missing'
        cleaned_data[col].append(raw_val)

print(" Global Descriptive Stats:")
for col in columns:
    dtype = column_types[col]
    values = cleaned_data[col]
    print(f" {col}:", end=" ")
    if dtype == 'numeric':
        stats = compute_numeric_stats(values)
    else:
        stats = compute_string_stats(values)
    print(stats)

# Grouped by 'id'
print("\n Grouped by id (first 3):")
grouped = defaultdict(list)
for row in rows:
    grouped[(row['id'])].append(row)

for key, group_rows in list(grouped.items())[:3]:
    print(f"\n=== id: {key} ===")
    group_data = defaultdict(list)
    for row in group_rows:
        for col in columns:
            val = clean_val(row[col])
            if val is None:
                val = '0.0' if column_types[col] == 'numeric' else 'missing'
            group_data[col].append(val)

    for col in columns:
        if column_types[col] == 'numeric':
            stats = compute_numeric_stats(group_data[col])
            if stats:
                print(f"{col:<45} | {stats}")

# Grouped by ('id', 'url')
print("\n Grouped by (id, url) (first 3):")
grouped = defaultdict(list)
for row in rows:
    grouped[(row['id'], row['url'])].append(row)

for key, group_rows in list(grouped.items())[:3]:
    print(f"\n=== id: {key[0]}, url: {key[1]} ===")
    group_data = defaultdict(list)
    for row in group_rows:
        for col in columns:
            val = clean_val(row[col])
            if val is None:
                val = '0.0' if column_types[col] == 'numeric' else 'missing'
            group_data[col].append(val)

    for col in columns:
        if column_types[col] == 'numeric':
            stats = compute_numeric_stats(group_data[col])
            if stats:
                print(f"{col:<45} | {stats}")
