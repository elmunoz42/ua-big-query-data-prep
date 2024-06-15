import pandas as pd

# Read data from the CSV file, skipping the first 6 rows
csv_file = 'data/twg/pages/pages-2019-q1.csv'
try:
    df = pd.read_csv(csv_file, skiprows=6)
except pd.errors.ParserError:
    print("Error reading CSV file. Please check the file format and structure.")
    exit()

# Exclude non-numeric columns (e.g., "Page") from summation
numeric_columns = df.select_dtypes(include='number')
total_row = numeric_columns.sum()
total_row['Page'] = 'Total'

# Create a new DataFrame with the total row
df_total = pd.DataFrame([total_row])

# Concatenate the original DataFrame with the total row
df = pd.concat([df, df_total], ignore_index=True)

print(df)