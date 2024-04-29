import pandas as pd
import os

directory_path = 'C:/Users/28905/Documents/NTU/semester2/CI/data/Skills/2012'

output_count = 0

for file_name in os.listdir(directory_path):
    if file_name.endswith('.csv') and output_count < 5:
        # Construct the full path to the csv file
        file_path = os.path.join(directory_path, file_name)

        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Check if 'JobID' column exists
        if 'JobID' not in df.columns:
            print(f"'JobID' column not found in {file_name}. Skipping this file.")
            continue

        # Group by 'JobID'
        grouped = df.groupby('JobID')

        for job_id, group_df in grouped:
            if output_count >= 5:
                break
            # Create a new filename with the JobID
            group_file_name = f"{file_name.split('.')[0]}_JobID_{job_id}.csv"
            group_file_path = os.path.join(directory_path, group_file_name)

            group_df.to_csv(group_file_path, index=False)

            output_count += 1

            if output_count >= 5:
                break

        if output_count >= 5:
            break

if output_count == 0:
    print("No 'JobID' groups found or no CSV files to process.")
else:
    print(f"Outputted {output_count} CSV files for different JobID groups.")