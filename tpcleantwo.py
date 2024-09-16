import os
import pandas as pd

def get_most_recent_file(directory):
    # Get the most recent file from the specified directory
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not files:
        raise FileNotFoundError("No CSV files found in the directory.")
    
    # Get full path of the files
    full_paths = [os.path.join(directory, f) for f in files]
    
    # Sort files by modification time and get the most recent one
    most_recent_file = max(full_paths, key=os.path.getmtime)
    
    return most_recent_file

def process_file(file_path):
    # Read the file without a header
    df = pd.read_csv(file_path, header=None)

    # Delete all rows that are completely blank
    df.dropna(how='all', inplace=True)

    # Delete rows that only contain data in the ninth column
    df = df[~((df.iloc[:, 8].notna()) & (df.iloc[:, :8].isna().all(axis=1)))]

    # For every blank cell in columns 1 through 3, copy the data from the cell above it
    df.iloc[:, :3] = df.iloc[:, :3].fillna(method='ffill')

    # Remove " 00:00:00" from every cell in the seventh column
    df[6] = df[6].astype(str).str.replace(" 00:00:00", "", regex=False)

    # Delete the very last row that contains data
    df = df.iloc[:-1]

    # Fill blank cells in the fifth column with "N/A"
    df[4] = df[4].fillna("N/A")

    # Delete the eighth column
    df = df.drop(columns=[7])

    # Overwrite the original file without header
    df.to_csv(file_path, index=False, header=False)

    print(f"File processed and overwritten: {file_path}")

def main():
    # Directory of the files
    directory = r"C:\Users\Public\Documents\TenantPrepays"
    
    # Get the most recent file
    recent_file = get_most_recent_file(directory)
    
    # Process and overwrite the file
    process_file(recent_file)

if __name__ == "__main__":
    main()