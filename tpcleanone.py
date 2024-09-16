import os
import pandas as pd

def get_most_recent_excel_file(directory):
    # Get the most recent Excel file from the specified directory
    excel_files = [f for f in os.listdir(directory) if f.endswith(('.xlsx', '.xls'))]
    if not excel_files:
        raise FileNotFoundError("No Excel files found in the directory.")
    
    # Get full path of the files
    full_paths = [os.path.join(directory, f) for f in excel_files]
    
    # Sort files by modification time and get the most recent one
    most_recent_file = max(full_paths, key=os.path.getmtime)
    
    return most_recent_file

def modify_excel_and_save_as_csv(file_path):
    # Read the Excel file without headers
    df = pd.read_excel(file_path, header=None)

    # Store the eight character suffix of the first column, third row
    suffix = str(df.iloc[2, 0])[-9:]

    # Delete the first four rows
    df = df.drop(index=[0, 1, 2, 3]).reset_index(drop=True)

    # Add the suffix to the second column cells if they contain data
    df[1] = df[1].apply(lambda x: str(x) + suffix if pd.notna(x) else x)

    # Delete the first column and shift the rest left
    df = df.drop(columns=[0])

    # Replace the original Excel file's extension with .csv
    csv_file_path = os.path.splitext(file_path)[0] + ".csv"

    # Save the modified DataFrame as a CSV, overwriting the original file (now as .csv)
    df.to_csv(csv_file_path, index=False, header=False)

    # Remove the original Excel file
    os.remove(file_path)

    print(f"File converted and saved as CSV: {csv_file_path}")
    
def main():
    # Directory of the Excel files
    directory = r"C:\Users\Public\Documents\TenantPrepays"
    
    # Get the most recent Excel file
    recent_file = get_most_recent_excel_file(directory)
    
    # Modify the Excel file, save it as CSV, and delete the original Excel file
    modify_excel_and_save_as_csv(recent_file)

if __name__ == "__main__":
    main()
