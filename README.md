
# Descriptive Analysis of 2024 U.S. Presidential Election Social Media Data

This repository provides exploratory data analysis and descriptive statistics for three datasets related to the 2024 U.S. Presidential Election:

1. `2024_fb_posts_president_scored_anon.csv` — Facebook posts
2. `2024_fb_ads_president_scored_anon.csv` — Facebook ads
3. `2024_tw_posts_president_scored_anon.csv` — Twitter posts

Each dataset was analyzed using:
- Pure Python (no third-party libraries)
- Pandas
- Polars
- Bonus: Supporting visualizations using `matplotlib` and `seaborn`

---

## How to Run

1. Clone the repository or download the scripts.
2. Place the CSV files in the same directory or adjust the file paths accordingly.
3. Run each of the three scripts (for Pure Python, Pandas, Polars) in your preferred environment:
   ```bash
   python pure_python_analysis.py
   python pandas_analysis.py
   python polars_analysis.py
   ```
4. Use Jupyter Notebooks provided for exploratory analysis and visualization.

---

## Data Handling

- Null values were handled by replacing with defaults: `0.0` for numeric, `"missing"` for string.
- Grouped descriptive statistics were computed using:
  - `Facebook_Id` and `post_id` for posts
  - `page_id` and `ad_id` for ads
  - `id` and `url` for Twitter posts

---

## Summary of Key Findings

### Facebook Posts:
- `message` and `link` fields were the most varied; some messages were reused.
- Most common language was `en`.
- `post_impressions`, `post_clicks`, and `post_engagements` show high variance across posts.

### Facebook Ads:
- Most ads were published in USD, and ad spend varied significantly.
- High concentration of ads from specific PACs (e.g., Texas Organizing Project PAC).
- States like Texas and California had the highest ad delivery.

### Twitter Posts:
- Extremely skewed engagement metrics (likes, views, retweets) indicating viral content.
- Top sources were `Twitter Web App` and `Twitter for iPhone`.
- Over 90% of the posts were in English.
- Many posts were labeled as `advocacy`, `issue`, or `attack` messages with relevant illumination topics like `economy`, `health`, and `incivility`.

---

## Visualizations

The Jupyter Notebooks include:
- Histograms and boxplots for numerical columns (likes, views, spend)
- Bar charts for top categories (publishers, languages, platforms)
- Time series plots by `month_year` to show temporal trends

---

## File Structure

```
├── FB_ADS_PRESIDENT_SCORED_ANON/
│ ├── pandas_stats.py
│ ├── polars_stats.py
│ ├── pure_python_stats.py
│ └── bonus_visualization.ipynb
├── FB_POSTS_PRESIDENT_SCORED_ANON/
│ ├── pandas_stats.py
│ ├── polars_stats.py
│ ├── pure_python_stats.py
│ └── bonus_visualization.ipynb
├── TWITTER_POSTS_PRESIDENT_SCORED_ANON/
│ ├── pandas_stats.py
│ ├── polars_stats.py
│ ├── pure_python_stats.py
│ └── bonus_visualization.ipynb
└── README.md
```

---



**End of README**
