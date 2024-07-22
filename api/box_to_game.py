import pandas as pd

# Specify the file path
input_file_path = './all_player_box_scores_2022_2023.csv'
output_file_path = './updated_game_data.csv'

# Read CSV data into a DataFrame
data = pd.read_csv(input_file_path)

# Sort the data by GAME_ID
data = data.sort_values(by='GAME_ID')

# Assign game number to each GAME_ID
data['GAME_NUMBER'] = data.groupby('GAME_ID').ngroup() + 1

# Reorder columns to place GAME_NUMBER at the front
columns = ['GAME_NUMBER'] + [col for col in data.columns if col != 'GAME_NUMBER']
data = data[columns]

# Save the updated DataFrame to a new CSV file
data.to_csv(output_file_path, index=False)

# Display the first 10 rows of the updated DataFrame
print(data.head(10))