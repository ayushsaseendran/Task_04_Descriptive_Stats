# Twitter Posts 2024 U.S. Presidential Dataset — Descriptive Analysis

##  Dataset
- **Filename**: `2024_tw_posts_president_scored_anon.csv`
- **Rows**: 27,304
- **Columns**: 47
- **Source**: Anonymized Twitter posts related to the 2024 U.S. Presidential election.

## Scripts Included

###  Script 1 — Pure Python (No Pandas, No Polars)
- Uses only `csv`, `math`, `collections`.
- Computes global and grouped stats:
  - Count, Mean, Min, Max, Std Dev (numeric)
  - Unique values, Most common (non-numeric)
- Grouping:
  - By `id`
  - By `(id, url)`

### Script 2 — Using Pandas
- Uses `pandas` for:
  - Global summary stats (`.describe()`, `.value_counts()`)
  - Grouped stats by `id` and `(id, url)`

### Script 3 — Using Polars
- Uses `polars` for optimized processing.
- Computes the same global and grouped stats as Pandas.

## Visualizations (Jupyter Notebook)
Using `matplotlib` and `seaborn`:
- Histograms of `likeCount`, `retweetCount`, `viewCount`
- Bar chart: Top sources (`source`)
- Line plot: Monthly trend using `month_year`
- Boxplot: Distribution of engagement across selected `illuminating` fields
- Heatmap: Correlation among numerical engagement metrics

## Summary of Key Findings

- **Engagement Extremes**: Posts received between 0 to **915K likes** and over **333M views**, with high standard deviation indicating a skewed distribution.
- **Dominant Language & Platform**: English (`en`) dominates with over 99%, and the top source is `Twitter Web App`.
- **Content Trends**:
  - Majority of posts have no reply/retweet relationship (`isReply`, `isRetweet` = False).
  - Frequent illumination on `advocacy`, `issue`, and `attack` topics.
- **Temporal Peaks**: High post counts in certain months (e.g., October 2024) suggest campaign-driven surges.

## How to Run the Code

1. Clone or download the script and dataset.
2. Make sure the file `2024_tw_posts_president_scored_anon.csv` is in the same directory.
3. Run the scripts:
   ```bash
   python descriptive_stats_pure_python.py
   python descriptive_stats_pandas.py
   python descriptive_stats_polars.py
   ```

   Or open the Jupyter notebook `tw_posts_analysis.ipynb` to see code and plots together.

## Requirements

```bash
pip install pandas polars matplotlib seaborn
```