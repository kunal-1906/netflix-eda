"""
Netflix Content Analysis - Exploratory Data Analysis
Author: Kunal Vig
Tools: Python, pandas, matplotlib, seaborn
Dataset: Netflix Movies & TV Shows
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({"figure.dpi": 150, "font.family": "DejaVu Sans"})
os.makedirs("outputs", exist_ok=True)

# ── 1. Load & Inspect ──────────────────────────────────────────────────────────
df = pd.read_csv("netflix_data.csv")

print("=" * 60)
print("NETFLIX DATASET — BASIC INFO")
print("=" * 60)
print(f"Shape          : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Missing values :\n{df.isnull().sum()}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nFirst 5 rows:\n{df.head()}")

# ── 2. Clean ───────────────────────────────────────────────────────────────────
df.dropna(inplace=True)
df["IMDb_Score"] = pd.to_numeric(df["IMDb_Score"], errors="coerce")
df["Release_Year"] = pd.to_numeric(df["Release_Year"], errors="coerce")
df.dropna(subset=["IMDb_Score", "Release_Year"], inplace=True)

print("\n" + "=" * 60)
print("CLEANING COMPLETE — Dataset ready for analysis")
print("=" * 60)

# ── 3. INSIGHT 1 — Content Type Distribution ──────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
type_counts = df["Type"].value_counts()
colors = ["#E50914", "#564d4d"]
wedges, texts, autotexts = ax.pie(
    type_counts, labels=type_counts.index, autopct="%1.1f%%",
    colors=colors, startangle=90, textprops={"fontsize": 13}
)
for at in autotexts:
    at.set_fontsize(12)
    at.set_color("white")
ax.set_title("Netflix Content: Movies vs TV Shows", fontsize=15, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("outputs/01_content_type_distribution.png")
plt.close()
print("\n✅ Chart 1 saved: Content Type Distribution")

# ── 4. INSIGHT 2 — Top 10 Genres ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
top_genres = df["Genre"].value_counts().head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, palette="Reds_r", ax=ax)
ax.set_title("Top 10 Genres on Netflix", fontsize=15, fontweight="bold")
ax.set_xlabel("Number of Titles", fontsize=12)
ax.set_ylabel("Genre", fontsize=12)
for i, v in enumerate(top_genres.values):
    ax.text(v + 0.2, i, str(v), va="center", fontsize=11)
plt.tight_layout()
plt.savefig("outputs/02_top_genres.png")
plt.close()
print("✅ Chart 2 saved: Top 10 Genres")

# ── 5. INSIGHT 3 — IMDb Score Distribution ────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
sns.histplot(df["IMDb_Score"], bins=15, kde=True, color="#E50914", ax=ax)
ax.axvline(df["IMDb_Score"].mean(), color="gold", linestyle="--", linewidth=2,
           label=f'Mean: {df["IMDb_Score"].mean():.2f}')
ax.set_title("IMDb Score Distribution of Netflix Content", fontsize=15, fontweight="bold")
ax.set_xlabel("IMDb Score", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("outputs/03_imdb_score_distribution.png")
plt.close()
print("✅ Chart 3 saved: IMDb Score Distribution")

# ── 6. INSIGHT 4 — Top 10 Countries ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
top_countries = df["Country"].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Blues_r", ax=ax)
ax.set_title("Top 10 Countries Producing Netflix Content", fontsize=15, fontweight="bold")
ax.set_xlabel("Number of Titles", fontsize=12)
ax.set_ylabel("Country", fontsize=12)
for i, v in enumerate(top_countries.values):
    ax.text(v + 0.2, i, str(v), va="center", fontsize=11)
plt.tight_layout()
plt.savefig("outputs/04_top_countries.png")
plt.close()
print("✅ Chart 4 saved: Top Countries")

# ── 7. INSIGHT 5 — IMDb Score by Genre (Top 8) ────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
top8_genres = df["Genre"].value_counts().head(8).index
df_top8 = df[df["Genre"].isin(top8_genres)]
sns.boxplot(data=df_top8, x="Genre", y="IMDb_Score", palette="Set2", ax=ax)
ax.set_title("IMDb Score Distribution by Genre (Top 8)", fontsize=15, fontweight="bold")
ax.set_xlabel("Genre", fontsize=12)
ax.set_ylabel("IMDb Score", fontsize=12)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("outputs/05_imdb_by_genre.png")
plt.close()
print("✅ Chart 5 saved: IMDb Score by Genre")

# ── 8. INSIGHT 6 — Content Released Per Year ──────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
yearly = df.groupby(["Release_Year", "Type"]).size().unstack(fill_value=0)
yearly.plot(kind="bar", ax=ax, color=["#E50914", "#564d4d"], edgecolor="white")
ax.set_title("Netflix Content Released Per Year by Type", fontsize=15, fontweight="bold")
ax.set_xlabel("Release Year", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)
ax.legend(title="Type", fontsize=11)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/06_content_per_year.png")
plt.close()
print("✅ Chart 6 saved: Content Per Year")

# ── 9. Correlation Heatmap ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
numeric_df = df[["IMDb_Score", "Release_Year", "Duration_Min", "Votes"]]
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax,
            linewidths=0.5, square=True)
ax.set_title("Correlation Heatmap — Numeric Features", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/07_correlation_heatmap.png")
plt.close()
print("✅ Chart 7 saved: Correlation Heatmap")

# ── 10. Key Insights Summary ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print("KEY INSIGHTS SUMMARY")
print("=" * 60)
print(f"1. Total titles analysed          : {len(df)}")
print(f"2. Movies vs TV Shows             : {type_counts.to_dict()}")
print(f"3. Most common genre              : {df['Genre'].value_counts().idxmax()}")
print(f"4. Average IMDb Score             : {df['IMDb_Score'].mean():.2f}")
print(f"5. Highest rated title            : {df.loc[df['IMDb_Score'].idxmax(), 'Title']} ({df['IMDb_Score'].max()})")
print(f"6. Lowest rated title             : {df.loc[df['IMDb_Score'].idxmin(), 'Title']} ({df['IMDb_Score'].min()})")
print(f"7. Top producing country          : {df['Country'].value_counts().idxmax()}")
print(f"8. Most votes (popular title)     : {df.loc[df['Votes'].idxmax(), 'Title']}")
print(f"9. Content growth (2020 vs 2018)  : {len(df[df['Release_Year']==2020])} vs {len(df[df['Release_Year']==2018])} titles")
print(f"10. Correlation IMDb & Votes      : {df['IMDb_Score'].corr(df['Votes']):.2f}")
print("=" * 60)
print("\n✅ All charts saved to /outputs folder. Analysis complete.")
