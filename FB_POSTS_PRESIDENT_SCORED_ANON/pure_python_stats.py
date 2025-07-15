import csv
import math
from collections import defaultdict, Counter

# --------------------------------------------
# Step 1: Helper functions
# --------------------------------------------

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
        'unique_values': len(set(values)),
        'most_common': freq.most_common(1)[0] if freq else None
    }

# --------------------------------------------
# Step 2: Load data
# --------------------------------------------

file_path = '../FB_POSTS_PRESIDENT_SCORED_ANON/2024_fb_posts_president_scored_anon.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    columns = reader.fieldnames

print(f"\n Loaded {len(rows)} rows and {len(columns)} columns.")

# --------------------------------------------
# Step 3: Infer column types
# --------------------------------------------

column_types = {}
for col in columns:
    sample = [clean_val(row[col]) for row in rows if clean_val(row[col]) is not None][:100]
    column_types[col] = 'numeric' if all(is_number(v) for v in sample) else 'string'

# --------------------------------------------
# Step 4: Clean data (fill nulls)
# --------------------------------------------

cleaned_data = defaultdict(list)
for col in columns:
    dtype = column_types[col]
    for row in rows:
        raw_val = clean_val(row[col])
        if raw_val is None:
            cleaned_data[col].append('0.0' if dtype == 'numeric' else 'missing')
        else:
            cleaned_data[col].append(raw_val)

# --------------------------------------------
# Step 5: Global Descriptive Stats
# --------------------------------------------

print("\n Global Descriptive Statistics:\n")
for col in columns:
    dtype = column_types[col]
    values = cleaned_data[col]

    print(f"\n {col} ({dtype}):")
    if dtype == 'numeric':
        stats = compute_numeric_stats(values)
    else:
        stats = compute_string_stats(values)

    for k, v in stats.items():
        print(f"  {k}: {v}")

# --------------------------------------------
# Step 6: Grouped by Facebook_Id
# --------------------------------------------

print("\n Grouped Statistics by Facebook_Id (First 3 Groups):\n")
grouped_by_page = defaultdict(list)
for row in rows:
    grouped_by_page[row['Facebook_Id']].append(row)

for page_id, group_rows in list(grouped_by_page.items())[:3]:
    print(f"\n=== Facebook_Id: {page_id} ===")
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

# --------------------------------------------
# Step 7: Grouped by Facebook_Id + post_id
# --------------------------------------------

print("\n Grouped Statistics by Facebook_Id + post_id (First 3 Groups):\n")
grouped_by_both = defaultdict(list)
for row in rows:
    key = (row['Facebook_Id'], row['post_id'])
    grouped_by_both[key].append(row)

for key, group_rows in list(grouped_by_both.items())[:3]:
    print(f"\n=== Facebook_Id: {key[0]}, post_id: {key[1]} ===")
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

# --------------------------------------------
# Step 8: Grouped by Page Category + post_id
# --------------------------------------------

print("\n Grouped Statistics by Page Category + post_id (First 3 Groups):\n")
if 'Page Category' in columns:
    grouped_by_pagecat = defaultdict(list)
    for row in rows:
        key = (row['Page Category'], row['post_id'])
        grouped_by_pagecat[key].append(row)

    for key, group_rows in list(grouped_by_pagecat.items())[:3]:
        print(f"\n=== Page Category: {key[0]}, post_id: {key[1]} ===")
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
else:
    print(" 'Page Category' column not found. Skipping this group.\n")
