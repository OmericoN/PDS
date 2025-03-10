import pandas as pd
import os

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file
csv_path = os.path.join(current_dir, 'data.csv')

# Read the CSV file
df = pd.read_csv(csv_path)

# Filter for ages greater than 19
df_filtered = df[df['Age'] > 19]

# Save the filtered dataframe back to the same CSV file
df_filtered.to_csv(csv_path, index=False)

print(f"Successfully filtered data. Saved {len(df_filtered)} records where Age > 19.")