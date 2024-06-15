import pandas as pd

def read_analytics_data(csv_file):
    try:
        df = pd.read_csv(csv_file, skiprows=6)
    except pd.errors.ParserError:
        print("Error reading CSV file. Please check the file format and structure.")
        return None

    # Exclude non-numeric columns (e.g., "Page") from summation
    numeric_columns = df.select_dtypes(include='number')
    total_row = numeric_columns.sum()
    total_row['Page'] = 'Total'

    # Create a new DataFrame with the total row
    df_total = pd.DataFrame([total_row])

    # Concatenate the original DataFrame with the total row
    df = pd.concat([df, df_total], ignore_index=True)

    return df

def extract_quarter_info(filename):
    # Extract the date range from the filename
    date_range = filename.split(" ")[-1].split(".")[0]
    start_date, end_date = date_range.split("-")
    start_month, start_day = start_date[:4], start_date[4:]
    end_month, end_day = end_date[:4], end_date[4:]

    # Convert month numbers to month names
    month_names = {
        "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
        "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
        "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
    }
    start_month_name = month_names.get(start_month, start_month)
    end_month_name = month_names.get(end_month, end_month)

    # Create the quarter info string
    quarter_info = f"{start_month_name} {start_day} - {end_month_name} {end_day}"

    return quarter_info