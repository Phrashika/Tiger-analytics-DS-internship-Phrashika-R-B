import pandas as pd

# -------------------------------
# Load IMDb Data
# -------------------------------
imdb = pd.read_csv("imdb.csv", on_bad_lines="skip", engine="python")
imdb.columns = imdb.columns.str.strip().str.lower()

# Confirm available columns
print("Columns:", imdb.columns.tolist())

# Correct column mappings
rating_col   = "imdbrating"     # rating column
title_col    = "title"          # title column
duration_col = "duration"       # duration in seconds
year_col     = "year"           # year (instead of release_date)

# -------------------------------
# Q7. IMDb rating for fifth movie
# -------------------------------
q7 = imdb.iloc[4][rating_col]
print("Q7: IMDb rating of 5th movie:", q7, "\n")

# -------------------------------
# Q8. Titles of shortest & longest runtime
# -------------------------------
q8 = {
    "shortest": imdb.loc[imdb[duration_col].idxmin(), title_col],
    "longest": imdb.loc[imdb[duration_col].idxmax(), title_col]
}
print("Q8: Shortest & Longest runtime movies:", q8, "\n")

# -------------------------------
# Q9. Sort by year (earliest first), then IMDb rating (highest first)
# -------------------------------
q9 = imdb.sort_values(by=[year_col, rating_col], ascending=[True, False])
print("Q9: Sorted by year & rating")
print(q9[[title_col, year_col, rating_col]].head(), "\n")

# -------------------------------
# Q10. Movies with duration 30–180 minutes
# (duration is in seconds → 30min=1800s, 180min=10800s)
# -------------------------------
q10 = imdb[(imdb[duration_col] >= 1800) & (imdb[duration_col] <= 10800)]
print("Q10: Movies 30–180 mins")
print(q10[[title_col, duration_col]].head(), "\n")