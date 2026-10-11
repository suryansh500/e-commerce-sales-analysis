E-Commerce Sales Analysis

Project Overview

This project analyzes e-commerce sales data using Python, Pandas, NumPy, Matplotlib, Seaborn, and SQL. It explores product performance, customer spending, revenue trends, order statuses, and city-wise sales.

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL

Dataset

The project uses three CSV files:

- "customers.csv" — customer details and cities
- "products.csv" — product names, categories, and prices
- "orders.csv" — order dates, quantities, discounts, payment methods, and order statuses

Key Analysis

- Total orders and customer counts
- Revenue by product and category
- Top five products by revenue
- Customer spending analysis
- City-wise revenue
- Monthly revenue trends
- Order status analysis
- Data visualization

Project Structure

ecommerce-sales-analysis/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
├── analysis.py
├── analysis.sql
├── requirements.txt
├── README.md
└── .gitignore

How to Run

1. Clone this repository.
2. Install the dependencies:
   "pip install -r requirements.txt"
3. Run the analysis:
   "python analysis.py"

Learning Outcomes

- Data cleaning and manipulation with Pandas
- Joining related datasets
- Grouping and aggregating data
- Time-based analysis
- Exploratory data analysis and visualization
- Writing SQL queries for business questions