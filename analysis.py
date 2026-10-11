# =========================================================
# E-COMMERCE SALES ANALYSIS
# Project 2
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# 1. LOAD THE DATA
# =========================================================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")


print("\n========== DATA OVERVIEW ==========")

print("Total customers:", len(customers))
print("Total products:", len(products))
print("Total orders:", len(orders))

print("\nCustomers:")
print(customers.head())

print("\nProducts:")
print(products.head())

print("\nOrders:")
print(orders.head())


# =========================================================
# 2. CHECK FOR MISSING VALUES
# =========================================================

print("\n========== MISSING VALUES ==========")

print("\nCustomers:")
print(customers.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())


# =========================================================
# 3. CLEAN THE ORDER DATA
# =========================================================

# Convert Order_Date into datetime format
orders["Order_Date"] = pd.to_datetime(
    orders["Order_Date"],
    errors="coerce"
)

# Make a copy of orders
orders_clean = orders.copy()

# Treat missing discounts as 0
orders_clean["Discount"] = orders_clean["Discount"].fillna(0)


# =========================================================
# 4. MERGE ORDERS WITH PRODUCTS
# =========================================================

merged = orders_clean.merge(
    products,
    on="Product_ID",
    how="left"
)


print("\n========== MERGED DATA ==========")

print(merged.head())

print("Number of merged rows:", len(merged))


# =========================================================
# 5. CALCULATE REVENUE
# =========================================================

merged["Revenue"] = (
    merged["Quantity"]
    * merged["Unit_Price"]
    * (1 - merged["Discount"])
)


print("\n========== CALCULATED REVENUE ==========")

print(
    "Total calculated order value: ₹",
    round(merged["Revenue"].sum(), 2)
)


# =========================================================
# 6. MERGE CUSTOMER INFORMATION
# =========================================================

merged2 = merged.merge(
    customers,
    on="Customer_ID",
    how="left"
)


# =========================================================
# 7. REVENUE BY PRODUCT
# =========================================================

product_revenue = (
    merged
    .groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY PRODUCT ==========")

print(product_revenue)


# =========================================================
# 8. TOP 5 PRODUCTS
# =========================================================

top_products = (
    merged
    .groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n========== TOP 5 PRODUCTS ==========")

print(top_products)


# =========================================================
# 9. REVENUE BY CATEGORY
# =========================================================

category_revenue = (
    merged
    .groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY CATEGORY ==========")

print(category_revenue)


# =========================================================
# 10. HIGHEST-REVENUE PRODUCT IN EACH CATEGORY
# =========================================================

product_category_revenue = (
    merged
    .groupby(
        ["Category", "Product_Name"]
    )["Revenue"]
    .sum()
    .reset_index()
)

top_product_by_category = (
    product_category_revenue.loc[
        product_category_revenue
        .groupby("Category")["Revenue"]
        .idxmax()
    ]
)

print(
    "\n========== TOP PRODUCT IN EACH CATEGORY =========="
)

print(top_product_by_category)


# =========================================================
# 11. REVENUE BY CITY
# =========================================================

city_revenue = (
    merged2
    .groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY CITY ==========")

print(city_revenue)


# =========================================================
# 12. TOP 5 CUSTOMERS
# =========================================================

customer_revenue = (
    merged2
    .groupby("Customer_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n========== TOP 5 CUSTOMERS ==========")

print(customer_revenue)


# =========================================================
# 13. MONTHLY REVENUE
# =========================================================

valid_dates = merged.dropna(
    subset=["Order_Date"]
).copy()

monthly_revenue = (
    valid_dates
    .groupby(
        valid_dates["Order_Date"].dt.to_period("M")
    )["Revenue"]
    .sum()
    .sort_index()
)

print("\n========== MONTHLY REVENUE ==========")

print(monthly_revenue)


# =========================================================
# 14. ORDER STATUS ANALYSIS
# =========================================================

status_counts = (
    orders_clean["Order_Status"]
    .value_counts()
)

status_revenue = (
    merged
    .groupby("Order_Status")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== ORDER COUNT BY STATUS ==========")

print(status_counts)

print(
    "\n========== CALCULATED ORDER VALUE BY STATUS =========="
)

print(status_revenue)


# =========================================================
# 15. TOP 5 PRODUCTS — BAR CHART
# =========================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title(
    "Top 5 Products by Calculated Order Value"
)

plt.xlabel("Revenue (₹)")
plt.ylabel("Product")

plt.tight_layout()
plt.show()


# =========================================================
# 16. REVENUE BY CATEGORY — BAR CHART
# =========================================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=category_revenue.index,
    y=category_revenue.values
)

plt.title(
    "Revenue by Product Category"
)

plt.xlabel("Category")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# =========================================================
# 17. MONTHLY REVENUE — LINE CHART
# =========================================================

plt.figure(figsize=(11, 5))

sns.lineplot(
    x=monthly_revenue.index.astype(str),
    y=monthly_revenue.values,
    marker="o"
)

plt.title(
    "Monthly Revenue Trend — 2025"
)

plt.xlabel("Month")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# =========================================================
# 18. ORDER STATUS — BAR CHART
# =========================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=orders_clean,
    x="Order_Status",
    order=status_counts.index
)

plt.title(
    "Number of Orders by Status"
)

plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=25)

plt.tight_layout()
plt.show()


# =========================================================
# 19. REVENUE BY CITY — BAR CHART
# =========================================================

plt.figure(figsize=(10, 5))

sns.barplot(
    x=city_revenue.index,
    y=city_revenue.values
)

plt.title(
    "Revenue by City"
)

plt.xlabel("City")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# =========================================================
# 20. END
# =========================================================

print("\n========== ANALYSIS COMPLETE ==========")
print("All analysis and visualizations are complete.")