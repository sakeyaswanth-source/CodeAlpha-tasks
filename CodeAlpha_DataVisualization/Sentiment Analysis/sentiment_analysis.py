import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer


# ============================================================
# CODEALPHA - TASK 4
# SENTIMENT ANALYSIS
# ============================================================

print("=" * 60)
print("          CODEALPHA - SENTIMENT ANALYSIS")
print("=" * 60)


# ============================================================
# 1. DOWNLOAD NLTK DATA
# ============================================================

print("\nDownloading NLTK sentiment data...")

nltk.download("vader_lexicon", quiet=True)

print("NLTK data ready.")


# ============================================================
# 2. CREATE SAMPLE REVIEW DATASET
# ============================================================

reviews = [
    ("This product is excellent and works perfectly", 5),
    ("I absolutely love this product", 5),
    ("Amazing quality and very useful", 5),
    ("The product is fantastic", 5),
    ("Very happy with my purchase", 5),

    ("Good product and reasonable quality", 4),
    ("I am satisfied with this purchase", 4),
    ("The product works well", 4),
    ("Pretty good product for the price", 4),
    ("I like the product", 4),

    ("The product is okay", 3),
    ("It is an average product", 3),
    ("Nothing special about this product", 3),
    ("The quality is acceptable", 3),
    ("It works as expected", 3),

    ("I don't like this product", 2),
    ("The quality is disappointing", 2),
    ("The product could be much better", 2),
    ("Not happy with the purchase", 2),
    ("The product has several problems", 2),

    ("Terrible product and very poor quality", 1),
    ("I hate this product", 1),
    ("Completely useless product", 1),
    ("Very disappointed with this purchase", 1),
    ("Worst product I have ever bought", 1),

    ("Excellent performance and great quality", 5),
    ("Really useful and easy to use", 5),
    ("The delivery was fast and the product was great", 5),
    ("Good quality but slightly expensive", 4),
    ("The product is decent and useful", 4),
    ("It is fine but could be improved", 3),
    ("Average quality for the price", 3),
    ("The product stopped working quickly", 2),
    ("Poor quality and disappointing service", 1),
    ("Very bad experience with this product", 1)
]


df = pd.DataFrame(
    reviews,
    columns=["Review", "Rating"]
)


print("\nSample dataset created.")

print("\nFirst 10 reviews:")
print(df.head(10))


# ============================================================
# 3. CHECK DATASET
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nRows:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ============================================================
# 4. TEXT CLEANING FUNCTION
# ============================================================

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


df["Cleaned_Review"] = df["Review"].apply(
    clean_text
)


# ============================================================
# 5. INITIALIZE SENTIMENT ANALYZER
# ============================================================

sia = SentimentIntensityAnalyzer()


# ============================================================
# 6. CALCULATE SENTIMENT SCORE
# ============================================================

def get_sentiment_score(text):

    score = sia.polarity_scores(text)

    return score["compound"]


df["Sentiment_Score"] = df["Cleaned_Review"].apply(
    get_sentiment_score
)


# ============================================================
# 7. CLASSIFY SENTIMENT
# ============================================================

def classify_sentiment(score):

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"


df["Sentiment"] = df["Sentiment_Score"].apply(
    classify_sentiment
)


# ============================================================
# 8. DISPLAY SENTIMENT RESULTS
# ============================================================

print("\n" + "=" * 60)
print("SENTIMENT ANALYSIS RESULTS")
print("=" * 60)

print(
    df[
        [
            "Review",
            "Rating",
            "Sentiment_Score",
            "Sentiment"
        ]
    ].to_string(index=False)
)


# ============================================================
# 9. SENTIMENT COUNTS
# ============================================================

sentiment_counts = (
    df["Sentiment"]
    .value_counts()
)

print("\n" + "=" * 60)
print("SENTIMENT COUNTS")
print("=" * 60)

print(sentiment_counts)


# ============================================================
# 10. SENTIMENT PERCENTAGE
# ============================================================

sentiment_percentage = (
    df["Sentiment"]
    .value_counts(normalize=True)
    * 100
)

print("\n" + "=" * 60)
print("SENTIMENT PERCENTAGE")
print("=" * 60)

print(
    sentiment_percentage.round(2)
)


# ============================================================
# 11. AVERAGE RATING BY SENTIMENT
# ============================================================

average_rating = (
    df.groupby("Sentiment")["Rating"]
    .mean()
    .round(2)
)

print("\n" + "=" * 60)
print("AVERAGE RATING BY SENTIMENT")
print("=" * 60)

print(average_rating)


# ============================================================
# 12. MOST POSITIVE REVIEWS
# ============================================================

print("\n" + "=" * 60)
print("TOP POSITIVE REVIEWS")
print("=" * 60)

positive_reviews = df.nlargest(
    5,
    "Sentiment_Score"
)

print(
    positive_reviews[
        [
            "Review",
            "Rating",
            "Sentiment_Score"
        ]
    ].to_string(index=False)
)


# ============================================================
# 13. MOST NEGATIVE REVIEWS
# ============================================================

print("\n" + "=" * 60)
print("TOP NEGATIVE REVIEWS")
print("=" * 60)

negative_reviews = df.nsmallest(
    5,
    "Sentiment_Score"
)

print(
    negative_reviews[
        [
            "Review",
            "Rating",
            "Sentiment_Score"
        ]
    ].to_string(index=False)
)


# ============================================================
# 14. CREATE VISUALIZATION FOLDER
# ============================================================

if not os.path.exists("visualizations"):

    os.makedirs("visualizations")


# ============================================================
# 15. SENTIMENT DISTRIBUTION BAR CHART
# ============================================================

plt.figure(
    figsize=(8, 6)
)

sns.countplot(
    data=df,
    x="Sentiment"
)

plt.title(
    "Sentiment Distribution"
)

plt.xlabel(
    "Sentiment"
)

plt.ylabel(
    "Number of Reviews"
)

plt.tight_layout()

plt.savefig(
    "visualizations/sentiment_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. SENTIMENT PIE CHART
# ============================================================

plt.figure(
    figsize=(8, 8)
)

plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Sentiment Percentage Distribution"
)

plt.tight_layout()

plt.savefig(
    "visualizations/sentiment_pie_chart.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. SENTIMENT BY RATING
# ============================================================

sentiment_rating = pd.crosstab(
    df["Rating"],
    df["Sentiment"]
)

sentiment_rating.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title(
    "Sentiment Distribution by Rating"
)

plt.xlabel(
    "Rating"
)

plt.ylabel(
    "Number of Reviews"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "visualizations/sentiment_by_rating.png",
    dpi=300
)

plt.close()


# ============================================================
# 18. SENTIMENT SCORE DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.histplot(
    data=df,
    x="Sentiment_Score",
    bins=15,
    kde=True
)

plt.title(
    "Distribution of Sentiment Scores"
)

plt.xlabel(
    "Compound Sentiment Score"
)

plt.ylabel(
    "Number of Reviews"
)

plt.tight_layout()

plt.savefig(
    "visualizations/sentiment_score_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 19. RATING VS SENTIMENT SCORE
# ============================================================

plt.figure(
    figsize=(9, 6)
)

sns.scatterplot(
    data=df,
    x="Rating",
    y="Sentiment_Score",
    s=80
)

plt.title(
    "Rating vs Sentiment Score"
)

plt.xlabel(
    "Rating"
)

plt.ylabel(
    "Sentiment Score"
)

plt.tight_layout()

plt.savefig(
    "visualizations/rating_vs_sentiment.png",
    dpi=300
)

plt.close()


# ============================================================
# 20. SAVE RESULTS
# ============================================================

df.to_csv(
    "sentiment_results.csv",
    index=False
)


# ============================================================
# 21. FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 60)
print("       SENTIMENT ANALYSIS COMPLETED")
print("=" * 60)

print(
    "\nTotal Reviews:",
    len(df)
)

print(
    "\nPositive Reviews:",
    (df["Sentiment"] == "Positive").sum()
)

print(
    "Negative Reviews:",
    (df["Sentiment"] == "Negative").sum()
)

print(
    "Neutral Reviews:",
    (df["Sentiment"] == "Neutral").sum()
)

print(
    "\nAverage Rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "\nAverage Sentiment Score:",
    round(
        df["Sentiment_Score"].mean(),
        3
    )
)

print(
    "\nResults saved as:"
)

print("sentiment_results.csv")

print(
    "\nVisualizations saved in:"
)

print("visualizations/")

print("\nTask 4 completed successfully!")

print("=" * 60)