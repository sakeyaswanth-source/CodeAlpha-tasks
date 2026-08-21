
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# -------------------------------------------------
# WEBSITE
# -------------------------------------------------

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# Store scraped books
books = []

# -------------------------------------------------
# SCRAPE 10 PAGES
# -------------------------------------------------

for page in range(1, 11):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    try:

        # Send request
        response = requests.get(
            url,
            timeout=10
        )

        # Check website response
        if response.status_code != 200:
            print(
                f"Page {page} could not be accessed."
            )
            continue

        # Convert HTML to BeautifulSoup
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Find all books
        book_list = soup.find_all(
            "article",
            class_="product_pod"
        )

        # Extract each book
        for book in book_list:

            # -----------------------------
            # TITLE
            # -----------------------------

            title = book.h3.a.get("title")

            # -----------------------------
            # PRICE
            # -----------------------------

            price = book.find(
                "p",
                class_="price_color"
            ).text.strip()

            # -----------------------------
            # RATING
            # -----------------------------

            rating = book.find(
                "p",
                class_="star-rating"
            )

            rating = rating.get("class")[1]

            # -----------------------------
            # AVAILABILITY
            # -----------------------------

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            # -----------------------------
            # STORE DATA
            # -----------------------------

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        # Small delay
        time.sleep(0.5)

    except requests.exceptions.RequestException as error:

        print(
            f"Error on page {page}: {error}"
        )


# -------------------------------------------------
# CREATE DATAFRAME
# -------------------------------------------------

df = pd.DataFrame(books)


# -------------------------------------------------
# CLEAN PRICE
# -------------------------------------------------

df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)


# -------------------------------------------------
# CONVERT RATING TO NUMBER
# -------------------------------------------------

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(
    rating_map
)


# -------------------------------------------------
# REMOVE DUPLICATES
# -------------------------------------------------

df.drop_duplicates(
    inplace=True
)

df.reset_index(
    drop=True,
    inplace=True
)


# -------------------------------------------------
# SAVE CSV
# -------------------------------------------------

df.to_csv(
    "books_dataset.csv",
    index=False
)


# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

print("\n")
print("=" * 50)
print("WEB SCRAPING COMPLETED")
print("=" * 50)

print(
    f"\nTotal books scraped: {len(df)}"
)

print("\nFirst 10 records:")
print(df.head(10))

print("\nDataset columns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset saved as:")
print("books_dataset.csv")

print("=" * 50)
