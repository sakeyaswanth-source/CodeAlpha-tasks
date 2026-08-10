import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================
# CODEALPHA - TASK 3
# DATA VISUALIZATION
# ============================================================

print("=" * 60)
print("       CODEALPHA - DATA VISUALIZATION")
print("=" * 60)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("cleaned_books.csv")

print("\nDataset loaded successfully!")

print("Number of books:", len(df))

print("\nFirst 5 records:")
print(df.head())


# ============================================================
# 2. CREATE CHARTS FOLDER
# ============================================================

if not os.path.exists("charts"):
    os.makedirs("charts")

print("\nCharts folder ready.")


# ============================================================
# CHART 1 - PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Price",
    bins=20,
    kde=True
)

plt.title(
    "Distribution of Book Prices",
    fontsize=16
)

plt.xlabel("Price")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "charts/01_price_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 2 - RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 6))

sns.countplot(
    data=df,
    x="Rating"
)

plt.title(
    "Distribution of Book Ratings",
    fontsize=16
)

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "charts/02_rating_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 3 - TOP 10 MOST EXPENSIVE BOOKS
# ============================================================

top_expensive = df.nlargest(
    10,
    "Price"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_expensive["Title"],
    top_expensive["Price"]
)

plt.title(
    "Top 10 Most Expensive Books",
    fontsize=16
)

plt.xlabel("Price")

plt.ylabel("Book Title")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "charts/03_top_10_expensive_books.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 4 - TOP 10 CHEAPEST BOOKS
# ============================================================

top_cheap = df.nsmallest(
    10,
    "Price"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_cheap["Title"],
    top_cheap["Price"]
)

plt.title(
    "Top 10 Cheapest Books",
    fontsize=16
)

plt.xlabel("Price")

plt.ylabel("Book Title")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "charts/04_top_10_cheapest_books.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 5 - PRICE VS RATING
# ============================================================

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Rating",
    y="Price",
    s=80
)

plt.title(
    "Relationship Between Book Rating and Price",
    fontsize=16
)

plt.xlabel("Rating")

plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    "charts/05_price_vs_rating.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 6 - AVERAGE PRICE BY RATING
# ============================================================

average_price_rating = (
    df.groupby("Rating")["Price"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(9, 6))

sns.barplot(
    data=average_price_rating,
    x="Rating",
    y="Price"
)

plt.title(
    "Average Book Price by Rating",
    fontsize=16
)

plt.xlabel("Rating")

plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig(
    "charts/06_average_price_by_rating.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 7 - PRICE DISTRIBUTION BY RATING
# ============================================================

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=df,
    x="Rating",
    y="Price"
)

plt.title(
    "Book Price Distribution by Rating",
    fontsize=16
)

plt.xlabel("Rating")

plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    "charts/07_price_distribution_by_rating.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 8 - CORRELATION HEATMAP
# ============================================================

correlation = df[
    ["Price", "Rating"]
].corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title(
    "Price and Rating Correlation",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    "charts/08_correlation_heatmap.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 9 - RATING PERCENTAGE
# ============================================================

rating_counts = (
    df["Rating"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 8))

plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Percentage of Books by Rating",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    "charts/09_rating_percentage.png",
    dpi=300
)

plt.show()


# ============================================================
# PRINT SUMMARY
# ============================================================

print("\n")
print("=" * 60)
print("             DATA ANALYSIS SUMMARY")
print("=" * 60)

print(
    "\nTotal Books:",
    len(df)
)

print(
    "Average Price:",
    round(df["Price"].mean(), 2)
)

print(
    "Minimum Price:",
    df["Price"].min()
)

print(
    "Maximum Price:",
    df["Price"].max()
)

print(
    "Average Rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "\nMost Common Rating:"
)

print(
    df["Rating"].mode()[0]
)


# ============================================================
# DISPLAY TOP EXPENSIVE BOOK
# ============================================================

most_expensive = df.loc[
    df["Price"].idxmax()
]

print("\nMost Expensive Book:")

print(
    most_expensive["Title"]
)

print(
    "Price:",
    most_expensive["Price"]
)


# ============================================================
# DISPLAY HIGHEST RATED BOOKS
# ============================================================

highest_rating = df["Rating"].max()

print(
    "\nHighest Rating:",
    highest_rating
)

print("\nBooks with highest rating:")

print(
    df[df["Rating"] == highest_rating][
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)


# ============================================================
# FINISH
# ============================================================

print("\n")
print("=" * 60)
print("       TASK 3 COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(
    "\nAll charts are saved inside the 'charts' folder."
)

