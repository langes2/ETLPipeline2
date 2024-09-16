import csv
import os
import glob
from collections import defaultdict

def get_latest_file(directory):
    # Find all CSV files in the specified directory
    list_of_files = glob.glob(os.path.join(directory, "*.csv"))
    
    # Return the most recently modified file
    if list_of_files:
        return max(list_of_files, key=os.path.getmtime)
    else:
        raise FileNotFoundError("No CSV files found in the specified directory.")

def check_duplicates_in_csv(file_path):
    # Dictionary to store how many times a combination of the specified columns has been seen
    seen_rows = defaultdict(int)
    updated_rows = []
    
    # Open the CSV file for reading
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)  # Read all rows in the file

        # Iterate through each row
        for row_number, row in enumerate(rows, start=1):
            # Extract values from columns 1, 2, 4, 6, and 7 (indices 0, 1, 3, 5, 6)
            key = (row[0], row[1], row[3], row[5], row[6])
            
            # Increment the seen counter for this combination of values
            seen_rows[key] += 1
            
            # If this is a duplicate, append the duplicate number (starting from 2)
            if seen_rows[key] > 1:
                row[5] = f"{row[5]} {seen_rows[key]}"
            
            updated_rows.append(row)

    # Write back the updated rows to the file
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(updated_rows)

# Example usage
directory = r"C:\Users\Public\Documents\TenantPrepays"
try:
    latest_file = get_latest_file(directory)
    print(f"Checking and updating file: {latest_file}")
    check_duplicates_in_csv(latest_file)
except FileNotFoundError as e:
    print(e)
