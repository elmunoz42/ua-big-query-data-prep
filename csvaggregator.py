import os
import pandas as pd
from helpers import read_analytics_data
from helpers import extract_quarter_info

# Prompt the user for the directory containing CSV files
csv_directory = input("Enter the path to the CSV files directory: ")

# Initialize an empty dataframe
combined_df = pd.DataFrame()

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)
        df = read_analytics_data(filepath)  # Use the custom function
        if df is not None:
            # Add an additional row with the quarter info
            quarter_info = extract_quarter_info(filename)
            df.loc[-1] = [quarter_info] + [None] * (df.shape[1] - 1)
            df.index = df.index + 1
            df.sort_index(inplace=True)
            combined_df = pd.concat([combined_df, df], axis=0)

# Create a results folder if it doesn't exist
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)

# Write the combined dataframe to a new CSV file in the results folder
report_name = input("Please provide the report name (with no spaces): ") + ".csv"
output_path = os.path.join(results_folder, report_name)
combined_df.to_csv(output_path, index=False)

print(f"Data aggregated successfully. Output saved to {report_name}")
