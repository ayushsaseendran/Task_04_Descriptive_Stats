import csv
import math
from collections import defaultdict, Counter

def clean(val):
    return val if val not in ("", "null", "None", "NA", "N/A") else None

def is_number(val):
    try:
        float(val)
        return True
    except:
        return False

def numeric_stats(values):
    nums = [float(v) for v in values if is_number(v)]
    if not nums:
        return None
    count = len(nums)
    mean = sum(nums) / count
    std = math.sqrt(sum((x - mean) ** 2 for x in nums) / count)
    return {"count": count, "mean": round(mean, 2), "min": round(min(nums), 2), "max": round(max(nums), 2), "std_dev": round(std, 2)}

def string_stats(values):
    values = [v for v in values if v is not None]
    freq = Counter(values)
    return {"count": len(values), "unique_values": len(set(values)), "most_common": freq.most_common(1)[0] if freq else None}

# Load CSV
with open("2024_fb_ads_president_scored_anon.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    cols = reader.fieldnames

print(f"\n Loaded {len(rows)} rows and {len(cols)} columns.")

# Infer types
types = {}
for col in cols:
    sample = [clean(row[col]) for row in rows[:100]]
    types[col] = "numeric" if all(is_number(v) for v in sample if v is not None) else "string"

# Global Stats
print("\n Global Descriptive Statistics:\n")
for col in cols:
    values = [clean(row[col]) for row in rows]
    print(f"{col} ({types[col]}):")
    stats = numeric_stats(values) if types[col] == "numeric" else string_stats(values)
    print(stats)

# Grouped by page_id (first 3)
print("\n Grouped by page_id (First 3):\n")
grouped_page = defaultdict(list)
for row in rows:
    grouped_page[row["page_id"]].append(row)

for pid, group_rows in list(grouped_page.items())[:3]:
    print(f"=== page_id: {pid} ===")
    for col in cols:
        if types[col] == "numeric":
            values = [clean(r[col]) for r in group_rows]
            stats = numeric_stats(values)
            if stats:
                print(f"{col:<45} | {stats}")

# Grouped by (page_id, ad_id)
print("\n Grouped by (page_id, ad_id) (First 3):\n")
grouped_both = defaultdict(list)
for row in rows:
    key = (row["page_id"], row["ad_id"])
    grouped_both[key].append(row)

for key, group_rows in list(grouped_both.items())[:3]:
    print(f"=== page_id: {key[0]}, ad_id: {key[1]} ===")
    for col in cols:
        if types[col] == "numeric":
            values = [clean(r[col]) for r in group_rows]
            stats = numeric_stats(values)
            if stats:
                print(f"{col:<45} | {stats}")
