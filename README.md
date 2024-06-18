# CSV Aggregator Script

This Python script aggregates data from multiple CSV files into a single combined CSV file. It’s useful when you have quarterly data split across different files and want to consolidate specific columns into one report.

## Introduction

When dealing with data spread across multiple CSV files, it’s common to need a consolidated view. Whether you’re working with quarterly financial reports, website analytics, or any other data split by time periods, this script simplifies the process of combining relevant columns into a single output.

## How It Works

User Input:
The script prompts the user for:
The path to the directory containing the CSV files.
A report name (without spaces) for the output file.
Data Aggregation:
The script reads each CSV file in the specified directory.
It skips the header row (assumed to be row 7) and selects columns 7a through 18b (adjust column indices as needed).
The data from all files is concatenated into a single dataframe.
Output:
The combined dataframe is saved to a new CSV file with the provided report name.
Usage
Clone this repository or create a new Python script.
Run the script.
Input the directory path and report name when prompted.
The aggregated data will be saved to the specified report name.
Example
Suppose you have quarterly sales data split across four CSV files (Q1.csv, Q2.csv, Q3.csv, and Q4.csv). Each file contains columns 7a through 18b representing sales data. Running this script will combine the relevant columns from all files into a single CSV report.

Feel free to customize the script to match your specific use case!
