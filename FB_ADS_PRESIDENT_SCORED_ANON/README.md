
# Descriptive Analysis of 2024 Facebook Ads (Presidential) Dataset

## Dataset
**File Name**: `2024_fb_ads_president_scored_anon.csv`  
**Rows**: 246,745  
**Columns**: 41

## Scripts Included
Three separate scripts were created to analyze this dataset:

1. **Pure Python (No Pandas, No Polars)**
   - Uses only standard libraries: `csv`, `math`, `collections`
   - Computes:
     - Count
     - Mean, Min, Max
     - Standard Deviation
     - Unique values and most frequent for categorical fields
   - Grouped stats computed for:
     - `page_id`
     - `page_id + ad_id`

2. **Pandas-based Script**
   - Uses `pandas` and `numpy`
   - Provides:
     - Global statistics via `.describe()`
     - Frequency analysis with `.value_counts()`, `.nunique()`
   - Grouped statistics using `.groupby()` and `.agg()`

3. **Polars-based Script**
   - Uses `polars` for faster computation on large datasets
   - Computes:
     - Descriptive statistics on numeric and string fields
     - Grouped stats for:
       - `page_id`
       - `page_id + ad_id`
     - Nulls handled and stats printed in a clean format

##  Visualizations
- **Numeric Distributions**
  - Histograms of `estimated_impressions`, `estimated_spend`, etc.
- **Categorical Analysis**
  - Bar chart of top publishers (`bylines`)
- **Topic Illuminations**
  - Count plot for most common political topics (`*_topic_illuminating`)

## Instructions to Run

1. Clone the repository or download the scripts.
2. Ensure you have Python 3.8+ installed.
3. Install dependencies:

```bash
pip install pandas polars matplotlib seaborn
```

4. Run any of the following scripts:

```bash
python analysis_pure_python_ads.py
python analysis_pandas_ads.py
python analysis_polars_ads.py
```

## Summary of Findings

- The dataset includes over **246k Facebook ads** from various political entities.
- Spend and impressions are heavily skewed with outliers.
- Most ads target a narrow geographic region, with states like Texas showing high delivery counts.
- `estimated_impressions` ranged from a few hundred to several million per ad.
- The `illuminating` topic scores show that the majority of ads scored low or zero on misinformation-related metrics.
- Some publishers are significantly more active than others, as seen in the top `bylines`.

---

This README provides a high-level overview. Refer to the individual scripts or notebook for full breakdowns.
