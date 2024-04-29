import os
import pandas as pd

directory_path = 'C:/Users/28905/Documents/NTU/semester2/CI/data/Skills/2012'

# Function to convert txt to CSV
def convert_txt_to_csv(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Read the txt file
            txt_data = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-separated values; change if needed
            # Construct CSV file path
            csv_file_path = file_path.replace('.txt', '.csv')
            # Write to CSV
            txt_data.to_csv(csv_file_path, index=False)
            print(f"Converted {filename} to CSV")

# Run the function - remember to update the 'directory_path' to the folder containing your files
convert_txt_to_csv('C:/Users/28905/Documents/NTU/semester2/CI/data/Skills/2012')