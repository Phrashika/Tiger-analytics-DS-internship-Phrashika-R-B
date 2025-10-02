import pandas as pd

# Load dataset
df = pd.read_excel(r"C:\Users\Buvaneswari V\Downloads\Module 3\Module 3\Data.xlsx")

# Rename columns for easier access
df = df.rename(columns={
    "Store Open": "opendate",
    "Store Modification Date": "remodeldate",
    "Store Close": "closuredate",
    "Total Sq Ft": "totalsqft",
    "Super Division": "superdivision",
    "Outlet Type": "outlettype",
    "State": "state",
    "Sales": "sales",
    "Year": "year",
    "Month": "month"
})

# Convert dates
for col in ["opendate", "remodeldate", "closuredate"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Ensure numerics
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["totalsqft"] = pd.to_numeric(df["totalsqft"], errors="coerce")

print("----- MARKET SALES ANALYSIS FOR CLIENT ABC -----\n")

# 1a. Total sales by year
print("1a. Total Sales by Year:")
print(df.groupby("year")["sales"].sum().sort_index(), "\n")

# 1b. Stores opened in 1991
print("1b. Stores opened in 1991:", df[df["opendate"].dt.year == 1991].shape[0], "\n")

# 1c. Stores remodelled
print("1c. Stores remodelled:", df[df["remodeldate"].notnull()].shape[0], "\n")

# 1d. Relationship between Sales & Sq.Ft
print("1d. Correlation between Sales & Sq.Ft:", df["sales"].corr(df["totalsqft"]), "\n")

# 1e. Most profitable Super Division
print("1e. Most Profitable Super Division (total sales):")
print(df.groupby("superdivision")["sales"].sum().sort_values(ascending=False), "\n")

# 1f. Active stores
print("1f. Active stores as of today:", df[df["closuredate"].isnull()].shape[0], "\n")

# 1g. Super Division with highest average Sq.Ft
print("1g. Super Division with highest average Sq.Ft:")
print(df.groupby("superdivision")["totalsqft"].mean().sort_values(ascending=False), "\n")

# 2a. Top 3 candidate states
print("2a. Top 3 candidate states (avg sales):")
print(df.groupby("state")["sales"].mean().sort_values(ascending=False).head(3), "\n")

# 2b. Best time of year to open a store
print("2b. Best time (month) to open store (avg sales):")
print(df.groupby("month")["sales"].mean().sort_values(ascending=False), "\n")

# 2c. Outlet type effect on store closures
print("2c. Outlet type effect on closures:")
print(df.groupby("outlettype")["closuredate"].apply(lambda x: x.notnull().sum()).sort_values(ascending=False))
