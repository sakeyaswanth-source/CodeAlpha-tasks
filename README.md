# 📊 CodeAlpha Data Analytics Internship Projects

## 📌 Project Overview

This repository contains the three projects completed as part of the **CodeAlpha Data Analytics Internship**.

The projects demonstrate a complete data analytics workflow:

**Web Scraping → Exploratory Data Analysis → Data Visualization**

The dataset used in the projects contains book information collected from the **Books to Scrape** demo website.

---

# 🚀 Project Workflow

```text
Books to Scrape Website
        ↓
   Task 1: Web Scraping
        ↓
 books_dataset.csv
        ↓
   Task 2: EDA
        ↓
 cleaned_books.csv
        ↓
 Task 3: Data Visualization
        ↓
 Charts & Insights
```

---

# 📚 Task 1 — Web Scraping

## Objective

The objective of Task 1 was to collect structured information from a public web page using Python web-scraping techniques.

## Website

**Books to Scrape**

```text
https://books.toscrape.com/
```

This is a demo website designed for practicing web scraping.

## Information Collected

The following information was extracted:

* 📖 Book Title
* 💰 Price
* ⭐ Rating
* 📦 Availability

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

## Process

1. Connected to the website using Requests.
2. Downloaded the webpage HTML.
3. Parsed the HTML using BeautifulSoup.
4. Located the required book information.
5. Extracted title, price, rating, and availability.
6. Cleaned the collected data.
7. Converted the data into a Pandas DataFrame.
8. Exported the dataset as a CSV file.

## Output

```text
books_dataset.csv
```

The dataset contains **200 book records** collected during the project.

---

# 📊 Task 2 — Exploratory Data Analysis

## Objective

The objective of Task 2 was to explore the scraped dataset, understand its structure, perform statistical analysis, identify patterns, and check for data-quality issues.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Analysis Performed

### Dataset Analysis

* Displayed the first and last records
* Checked dataset dimensions
* Examined column names
* Checked data types
* Generated statistical summaries
* Checked missing values
* Checked duplicate records

### Statistical Analysis

Calculated:

* Average book price
* Minimum book price
* Maximum book price
* Median book price
* Average rating
* Price by rating
* Price and rating correlation

### Additional Analysis

Identified:

* Most expensive books
* Cheapest books
* Highest-rated books
* Lowest-rated books
* Rating distribution
* Potential price outliers

## Visualizations Created

* Price distribution
* Rating distribution
* Price boxplot
* Rating vs. price
* Correlation heatmap

## Output

```text
cleaned_books.csv
```

---

# 📈 Task 3 — Data Visualization

## Objective

The objective of Task 3 was to transform the analyzed data into meaningful visualizations and communicate important patterns and relationships clearly.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Visualizations Created

### 1. Price Distribution

Shows how book prices are distributed across the dataset.

### 2. Rating Distribution

Shows the number of books available for each rating.

### 3. Top 10 Most Expensive Books

Displays the ten books with the highest prices.

### 4. Top 10 Cheapest Books

Displays the ten books with the lowest prices.

### 5. Price vs Rating

Shows the relationship between book ratings and prices.

### 6. Average Price by Rating

Compares the average price of books across different ratings.

### 7. Price Distribution by Rating

Uses a boxplot to compare price distributions and identify potential outliers for each rating.

### 8. Correlation Heatmap

Displays the correlation between numerical variables such as price and rating.

### 9. Rating Percentage

Shows the percentage distribution of books across different ratings.

---

# 📁 Project Structure

```text
CodeAlpha_DataVisualization/
│
├── cleaned_books.csv
├── visualization.py
├── README.md
│
└── charts/
    │
    ├── 01_price_distribution.png
    ├── 02_rating_distribution.png
    ├── 03_top_10_expensive_books.png
    ├── 04_top_10_cheapest_books.png
    ├── 05_price_vs_rating.png
    ├── 06_average_price_by_rating.png
    ├── 07_price_distribution_by_rating.png
    ├── 08_correlation_heatmap.png
    └── 09_rating_percentage.png
```

---

# 🛠️ Installation

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 pandas numpy matplotlib seaborn
```

---

# ▶️ How to Run

## Task 1 — Web Scraping

Open the Web Scraping project folder:

```bash
cd CodeAlpha_WebScraping
```

Run:

```bash
python webScraping.py
```

This creates:

```text
books_dataset.csv
```

---

## Task 2 — EDA

Place `books_dataset.csv` inside the EDA project folder.

Run:

```bash
python eda.py
```

This performs data exploration and creates:

```text
cleaned_books.csv
```

---

## Task 3 — Data Visualization

Place `cleaned_books.csv` inside the Data Visualization project folder.

Run:

```bash
python visualization.py
```

The charts will be saved inside:

```text
charts/
```

---

# 💡 Key Skills Demonstrated

Through these three projects, I gained practical experience in:

* Python Programming
* Web Scraping
* Requests
* BeautifulSoup
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Statistical Analysis
* Matplotlib
* Seaborn
* Data Visualization
* Data Interpretation
* GitHub Project Management

---

# 🔄 Complete Data Analytics Pipeline

This internship project demonstrates the complete workflow:

### Step 1 — Data Collection

Data was collected from the Books to Scrape website using Python.

### Step 2 — Data Cleaning

The collected data was cleaned and converted into suitable formats.

### Step 3 — Exploratory Analysis

The dataset was analyzed to understand its structure, statistics, distributions, and relationships.

### Step 4 — Visualization

The findings were communicated using multiple charts and graphs.

### Step 5 — Insights

The visualizations help understand:

* Book price distributions
* Rating distributions
* Expensive and inexpensive books
* Relationship between price and rating
* Average price across ratings
* Correlations between numerical variables

---

# 🎯 Internship Tasks Completed

| Task   | Project                   | Status      |
| ------ | ------------------------- | ----------- |
| Task 1 | Web Scraping              | ✅ Completed |
| Task 2 | Exploratory Data Analysis | ✅ Completed |
| Task 3 | Data Visualization        | ✅ Completed |

---

# 👨‍💻 Author

**Yaswanth**

Data Analytics Intern
CodeAlpha Internship

---

# 📌 Acknowledgement

This project was completed as part of the **CodeAlpha Data Analytics Internship**, providing hands-on experience in data collection, data analysis, and data visualization using Python.
