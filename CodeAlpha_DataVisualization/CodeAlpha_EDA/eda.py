import os

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as exc:
    missing_pkg = exc.name if hasattr(exc, "name") else str(exc)
    print(f"Missing required package: {missing_pkg}")
    print("Install dependencies with: pip install pandas matplotlib")
    raise SystemExit(1)

# =====================================================
# CODEALPHA - EXPLORATORY DATA ANALYSIS
# =====================================================

print("=" * 60)
print("       CODEALPHA - EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# =====================================================
# 1. LOAD DATASET
# =====================================================

df = pd.read_csv("books_dataset.csv")

print("\n1. DATASET LOADED SUCCESSFULLY")


# =====================================================
# 2. DISPLAY FIRST 5 RECORDS
# =====================================================

print("\n2. FIRST 5 RECORDS")
print("-" * 40)

print(df.head())


# =====================================================
# 3. DISPLAY LAST 5 RECORDS
# =====================================================

print("\n3. LAST 5 RECORDS")
print("-" * 40)

print(df.tail())


# =====================================================
# 4. DATASET SIZE
# =====================================================

print("\n4. DATASET SIZE")
print("-" * 40)

rows, columns = df.shape

print("Number of rows:", rows)
print("Number of columns:", columns)


# =====================================================
# 5. COLUMN NAMES
# =====================================================

print("\n5. COLUMN NAMES")
print("-" * 40)

print(df.columns.tolist())


# =====================================================
# 6. DATA TYPES
# =====================================================

print("\n6. DATA TYPES")
print("-" * 40)

print(df.dtypes)


# =====================================================
# 7. DATASET INFORMATION
# =====================================================

print("\n7. DATASET INFORMATION")
print("-" * 40)

df.info()


# =====================================================
# 8. STATISTICAL SUMMARY
# =====================================================

print("\n8. STATISTICAL SUMMARY")
print("-" * 40)

print(df.describe())


# =====================================================
# 9. MISSING VALUES
# =====================================================

print("\n9. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)


# =====================================================
# 10. DUPLICATE VALUES
# =====================================================

print("\n10. DUPLICATE RECORDS")
print("-" * 40)

duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)


# =====================================================
# 11. UNIQUE RATINGS
# =====================================================

print("\n11. UNIQUE RATINGS")
print("-" * 40)

print(df["Rating"].unique())


# =====================================================
# 12. RATING COUNTS
# =====================================================

print("\n12. RATING COUNTS")
print("-" * 40)

rating_counts = df["Rating"].value_counts().sort_index()

print(rating_counts)


# =====================================================
# 13. AVERAGE PRICE
# =====================================================

print("\n13. AVERAGE PRICE")
print("-" * 40)

average_price = df["Price"].mean()

print(
    "Average book price:",
    round(average_price, 2)
)


# =====================================================
# 14. MINIMUM PRICE
# =====================================================

print("\n14. MINIMUM PRICE")
print("-" * 40)

minimum_price = df["Price"].min()

print(
    "Minimum book price:",
    minimum_price
)


# =====================================================
# 15. MAXIMUM PRICE
# =====================================================

print("\n15. MAXIMUM PRICE")
print("-" * 40)

maximum_price = df["Price"].max()

print(
    "Maximum book price:",
    maximum_price
)


# =====================================================
# 16. MEDIAN PRICE
# =====================================================

print("\n16. MEDIAN PRICE")
print("-" * 40)

median_price = df["Price"].median()

print(
    "Median book price:",
    median_price
)


# =====================================================
# 17. AVERAGE RATING
# =====================================================

print("\n17. AVERAGE RATING")
print("-" * 40)

average_rating = df["Rating"].mean()

print(
    "Average rating:",
    round(average_rating, 2)
)


# =====================================================
# 18. MOST EXPENSIVE BOOKS
# =====================================================

print("\n18. TOP 10 MOST EXPENSIVE BOOKS")
print("-" * 40)

expensive_books = df.nlargest(
    10,
    "Price"
)

print(
    expensive_books[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)


# =====================================================
# 19. CHEAPEST BOOKS
# =====================================================

print("\n19. TOP 10 CHEAPEST BOOKS")
print("-" * 40)

cheapest_books = df.nsmallest(
    10,
    "Price"
)

print(
    cheapest_books[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)


# =====================================================
# 20. HIGHEST RATED BOOKS
# =====================================================

print("\n20. HIGHEST RATED BOOKS")
print("-" * 40)

highest_rated = df.nlargest(
    10,
    "Rating"
)

print(
    highest_rated[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)


# =====================================================
# 21. LOWEST RATED BOOKS
# =====================================================
print("\n21. LOWEST RATED BOOKS")
print("-" * 40)

lowest_rated = df.nsmallest(
    10,
    "Rating"
)

print(
    lowest_rated[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)


# =====================================================
# 22. AVERAGE PRICE BY RATING
# =====================================================

print("\n22. AVERAGE PRICE BY RATING")
print("-" * 40)

average_price_rating = (
    df.groupby("Rating")["Price"]
    .mean()
    .round(2)
)

print(average_price_rating)

# =====================================================
# 23. CORRELATION
# =====================================================

print("\n23. PRICE AND RATING CORRELATION")
print("-" * 40)

correlation = df[
    ["Price", "Rating"]
].corr()

print(correlation)


# =====================================================
# 24. CREATE VISUALIZATION FOLDER
# =====================================================

if not os.path.exists("eda_visualizations"):
    os.makedirs("eda_visualizations")


# =====================================================
# 25. PRICE DISTRIBUTION
# =====================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=20
)

plt.title(
    "Distribution of Book Prices"
)

plt.xlabel("Price")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "eda_visualizations/price_distribution.png",
    dpi=300
)

plt.show()


# =====================================================
# 26. RATING DISTRIBUTION
# =====================================================

plt.figure(figsize=(8, 6))

rating_counts.plot(
    kind="bar"
)

plt.title(
    "Book Rating Distribution"
)

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "eda_visualizations/rating_distribution.png",
    dpi=300
)

plt.show()


# =====================================================
# 27. PRICE BOXPLOT
# =====================================================

plt.figure(figsize=(8, 6))

plt.boxplot(df["Price"], vert=False)

plt.title(
    "Book Price Distribution and Outliers"
)

plt.xlabel("Price")

plt.tight_layout()

plt.savefig(
    "eda_visualizations/price_boxplot.png",
    dpi=300
)

plt.show()


# =====================================================
# 28. RATING VS PRICE
# =====================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Rating"],
    df["Price"]
)

plt.title(
    "Relationship Between Rating and Price"
)

plt.xlabel("Rating")

plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    "eda_visualizations/rating_vs_price.png",
    dpi=300
)

plt.show()


# =====================================================
# 29. CORRELATION HEATMAP
# =====================================================

plt.figure(figsize=(7, 5))

plt.imshow(
    correlation,
    cmap="coolwarm",
    aspect="auto",
    vmin=-1,
    vmax=1
)

for i in range(correlation.shape[0]):
    for j in range(correlation.shape[1]):
        plt.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            color="black"
        )

plt.xticks([0, 1], correlation.columns)
plt.yticks([0, 1], correlation.index)
plt.colorbar()

plt.title(
    "Price and Rating Correlation"
)

plt.tight_layout()

plt.savefig(
    "eda_visualizations/correlation_heatmap.png",
    dpi=300
)

plt.show()


# =====================================================
# 30. SAVE CLEANED DATASET
# =====================================================

df.to_csv(
    "cleaned_books.csv",
    index=False
)


# =====================================================
# FINAL SUMMARY
# =====================================================

print("\n")
print("=" * 60)
print("       EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    "\nTotal books:",
    len(df)
)

print(
    "Average price:",
    round(df["Price"].mean(), 2)
)

print(
    "Average rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "Minimum price:",
    df["Price"].min()
)

print(
    "Maximum price:",
    df["Price"].max()
)

print(
    "Duplicate records:",
    df.duplicated().sum()
)

print(
    "\nCleaned dataset saved as:"
)

print("cleaned_books.csv")

print(
    "\nCharts saved inside:"
)

print("eda_visualizations/")

print("\nEDA TASK COMPLETED!")
print("=" * 60)

