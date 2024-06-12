import pandas as pd
import os

# Prompt the user for the directory containing CSV files
csv_directory = input("Enter the path to the CSV files directory: ")

# Prompt the user for the report name
report_name = input("Please provide the report name (with no spaces): ")

# Initialize an empty dataframe
combined_df = pd.DataFrame()

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)
        # Read data from the CSV file (skip the header row)
        df = pd.read_csv(filepath, skiprows=6)  # Skip the first 7 rows (0-based indexing)
        # Select columns 7a through 18b (adjust column names as needed)
        selected_columns = df.iloc[:, 6:29]  # Assuming 0-based indexing
        # Concatenate with the combined dataframe
        combined_df = pd.concat([combined_df, selected_columns], axis=0)

# Write the combined dataframe to a new CSV file
combined_df.to_csv(report_name, index=False)

print(f"Data aggregated successfully. Output saved to {report_name}")

