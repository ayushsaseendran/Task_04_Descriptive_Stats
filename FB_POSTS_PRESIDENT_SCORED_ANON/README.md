# Descriptive Analysis of 2024 Facebook Posts (Presidential Election)

This project performs an in-depth descriptive statistical analysis on the `2024_fb_posts_president_scored_anon.csv` dataset. The analysis includes summaries of numeric and categorical columns, handling of nulls, grouped statistics, and visualizations. Three separate implementations are provided: one using **pure Python**, another using **Pandas**, and a third using **Polars**.  

---

## How to Run

1. **Clone or download the repository.**
2. Ensure you have Python 3.8+ installed.
3. Install dependencies (for Pandas/Polars scripts):
   ```bash
   pip install pandas polars matplotlib seaborn
   ```
4. Run each script in a Jupyter Notebook or Python file:
   - `pure_python_analysis.py`
   - `pandas_analysis.ipynb`
   - `polars_analysis.py`

---

## Script Descriptions

### 1. `pure_python_analysis.py`
- Uses only Python's built-in libraries (`csv`, `math`, `collections`).
- Calculates:
  - Count, Mean, Min, Max, Std Dev (numeric)
  - Unique counts & most frequent values (categorical)
- Grouped analyses by:
  - `Facebook_Id`
  - `Facebook_Id + post_id`

### 2. `pandas_analysis.ipynb`
- Uses **pandas** for descriptive statistics.
- Includes:
  - `.describe()`, `.value_counts()`, `.nunique()`
  - Grouped `.agg()` summaries
  - Bonus visualizations using `matplotlib` and `seaborn`

### 3. `polars_analysis.py`
- Uses **Polars** for fast computation on large datasets.
- Efficient `.describe()`, `.group_by()`, and aggregations.
- Grouped analysis by:
  - `Facebook_Id`
  - `Facebook_Id + post_id`
- Fixed display formatting for standard deviation and null-safe printing.

---

## Summary of Findings

- **Engagement Distribution**: Highly skewed — few posts account for the majority of likes, shares, and comments.
- **Language**: English (`'en'`) dominates the dataset.
- **Message Types**: Posts often center around **issue** and **advocacy messaging**. **Attack** and **scam-related content** are present but less common.
- **Page Behavior**: Some Facebook pages are significantly more active and polarizing.
- **Grouped Insights**:
  - By `Facebook_Id`: Revealed patterns in tone (e.g., pages frequently using attack/incivility messaging).
  - By `Facebook_Id + post_id`: Helped identify reposted or amplified content.
- **Null Handling**: Minor nulls in fields like `image_text`, `headline`, and `message`; handled gracefully in analysis.

---

## Visualizations Included

- Histogram of engagement metrics (likes, shares, etc.)
- Bar chart of top posting pages
- Boxplots for outlier detection
- Count plots for categorical variables

---

##  Tools & Libraries

- Python 3.8+
- Pandas
- Polars
- Matplotlib
- Seaborn

---

## Dataset

- `2024_fb_posts_president_scored_anon.csv`
- Shape: 19009 rows × 56 columns
- Includes fields for message content, post timing, engagement metrics, and illuminating scores on incivility, fraud, etc.

---

## Author

This analysis was prepared as part of a research task focused on descriptive analytics for election-related social media datasets.

---