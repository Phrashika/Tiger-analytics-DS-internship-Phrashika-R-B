import pandas as pd

# -------------------------------
# Load Sales Data
# -------------------------------
sales = pd.read_excel("SalesData.xlsx")

# Normalize column names (remove spaces, lowercase)
sales.columns = sales.columns.str.strip().str.lower()

# -------------------------------
# Q1. Least amount sale that was done for each item
# -------------------------------
q1 = sales.groupby("item")["sale_amt"].min().reset_index()
print("Q1: Least amount sale per item")
print(q1, "\n")

# -------------------------------
# Q2. Total sales for each year and region
# -------------------------------
sales["orderdate"] = pd.to_datetime(sales["orderdate"], errors="coerce")
sales["year"] = sales["orderdate"].dt.year
q2 = sales.groupby(["year", "region"])["sale_amt"].sum().reset_index()
print("Q2: Total sales by year and region")
print(q2, "\n")

# -------------------------------
# Q3. Create new column 'days_diff'
# -------------------------------
reference_date = pd.to_datetime("2025-01-01")  # you can change the reference date
sales["days_diff"] = (reference_date - sales["orderdate"]).dt.days
print("Q3: Added 'days_diff' column")
print(sales[["orderdate", "days_diff"]].head(), "\n")

# -------------------------------
# Q4. Manager → list of salesmen
# -------------------------------
q4 = sales.groupby("manager")["salesman"].unique().reset_index()
q4.rename(columns={"salesman": "list_of_salesmen"}, inplace=True)
print("Q4: Manager with their salesmen")
print(q4, "\n")

# -------------------------------
# Q5. Number of salesmen & total sales per region
# -------------------------------
q5 = sales.groupby("region").agg(
    salesmen_count=("salesman", "nunique"),
    total_sales=("sale_amt", "sum")
).reset_index()
print("Q5: Salesmen count and total sales by region")
print(q5, "\n")

# -------------------------------
# Q6. Total sales as percentage for each manager
# -------------------------------
manager_sales = sales.groupby("manager")["sale_amt"].sum()
q6 = (manager_sales / manager_sales.sum() * 100).reset_index()
q6.columns = ["manager", "percent_sales"]
print("Q6: Manager sales as percentage")
print(q6, "\n")