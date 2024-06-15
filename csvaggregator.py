import pandas as pd
import os 
from helpers import read_analytics_data
# from helpers import extract_quarter_info

# Prompt the user for the directory containing CSV files
csv_directory = input("Enter the path to the CSV files directory: ")

# Prompt the user for the report name
report_name = input("Please provide the report name (with no spaces): ")

# Read data from the CSV files using the custom function
combined_df = pd.DataFrame()
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)
        df = read_analytics_data(filepath)  # Use the custom function
        if df is not None:
            combined_df = pd.concat([combined_df, df], axis=0)

# Write the combined dataframe to a new CSV file
combined_df.to_csv(report_name, index=False)

print(f"Data aggregated successfully. Output saved to {report_name}")

