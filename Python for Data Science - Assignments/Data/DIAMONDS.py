import pandas as pd
import numpy as np

# -------------------------------
# Load Diamonds Data
# -------------------------------
diamonds = pd.read_csv("diamonds.csv")
diamonds.columns = diamonds.columns.str.strip().str.lower()

# -------------------------------
# Q11. Count duplicate rows
# -------------------------------
q11 = diamonds.duplicated().sum()
print("Q11: Duplicate rows count =", q11, "\n")

# -------------------------------
# Q12. Drop rows with missing values in carat and cut
# -------------------------------
q12 = diamonds.dropna(subset=["carat", "cut"])
print("Q12: Data after dropping rows with missing carat & cut")
print(q12.head(), "\n")

# -------------------------------
# Q13. Subset with only numeric columns
# -------------------------------
q13 = diamonds.select_dtypes(include=[np.number])
print("Q13: Numeric columns subset")
print(q13.head(), "\n")

# -------------------------------
# Q14. Compute volume = x*y*z if depth > 60 else 8
# -------------------------------
diamonds["volume"] = np.where(
    diamonds["depth"] > 60,
    diamonds["x"] * diamonds["y"] * diamonds["z"],
    8
)
print("Q14: Added 'volume' column")
print(diamonds[["depth", "x", "y", "z", "volume"]].head(), "\n")

# -------------------------------
# Q15. Impute missing price values with mean (⚡ no FutureWarning)
# -------------------------------
diamonds["price"] = diamonds["price"].fillna(diamonds["price"].mean())
print("Q15: Price column after imputing mean")
print(diamonds[["price"]].head(), "\n")