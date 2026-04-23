# 🎬 Netflix Content Analysis — Exploratory Data Analysis

An end-to-end Exploratory Data Analysis (EDA) project on Netflix Movies and TV Shows using Python.

## 📌 Objective
To analyse Netflix's content library and uncover trends in genres, ratings, countries, and content growth over the years using data cleaning, analysis, and visualisation techniques.

## 🛠️ Tools & Technologies
- **Python** — Core programming language
- **pandas** — Data loading, cleaning, and manipulation
- **matplotlib** — Data visualisation
- **seaborn** — Statistical visualisation

## 📊 Key Insights
1. **55% TV Shows vs 45% Movies** on Netflix
2. **Drama** is the most common genre, followed by Crime and Sci-Fi
3. Average IMDb Score across all content: **7.27**
4. **Scam 1992** is the highest rated title (9.3) — India's content is top-tier
5. **USA** dominates content production, followed by UK and India
6. **Stranger Things** has the highest number of votes (1.2M) — most popular title
7. Moderate positive correlation (0.41) between IMDb Score and Votes
8. Netflix content releases nearly **doubled from 2018 to 2020**

## 📁 Project Structure
```
netflix-eda/
│
├── netflix_data.csv          # Dataset (100 Netflix titles)
├── netflix_eda.py            # Main analysis script
├── outputs/                  # Generated charts
│   ├── 01_content_type_distribution.png
│   ├── 02_top_genres.png
│   ├── 03_imdb_score_distribution.png
│   ├── 04_top_countries.png
│   ├── 05_imdb_by_genre.png
│   ├── 06_content_per_year.png
│   └── 07_correlation_heatmap.png
└── README.md
```

## ▶️ How to Run
```bash
# Clone the repo
git clone https://github.com/kunal-1906/netflix-eda.git
cd netflix-eda

# Install dependencies
pip install pandas matplotlib seaborn

# Run the analysis
python netflix_eda.py
```

## 📈 Sample Visualisations
Charts are saved in the `/outputs` folder after running the script.

---
**Author:** Kunal Vig | [LinkedIn](https://linkedin.com/in/kunal-tiet) | [GitHub](https://github.com/kunal-1906)
