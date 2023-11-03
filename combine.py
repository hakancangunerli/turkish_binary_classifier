import pandas as pd
import os

# Path to the directory containing the CSVs
data_directory = './data/'

# Name for the combined CSV file
output_filename = './combined_data.csv'

# Check if the combined CSV already exists; if not, create one with headers only
if not os.path.exists(output_filename):
    with open(output_filename, 'w') as f:
        pass

# Loop through each file in the directory
for filename in os.listdir(data_directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(data_directory, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath, low_memory=False)

        # Append the data to the combined CSV (without headers, but ensuring columns match)
        df.to_csv(output_filename, mode='a', header=False if os.path.getsize(output_filename) > 0 else True, index=False)

        # Print the name of the file being processed
        print(f"Processed: {filename}")

print("All CSVs combined successfully!")
