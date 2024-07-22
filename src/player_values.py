import json
import csv

# Load your JSON data
with open('../nba2k-player-ratings/data/league.json', 'r') as file:
    data = json.load(file)

# Function to write data to a CSV file
def write_to_csv(data, output_file):
    # Define the CSV file header
    header = ['id', 'overall', 'price', 'player', 'team']
    
    # Open the CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        
        # Write the header to the CSV file
        writer.writeheader()
        
        # Write the data rows to the CSV file
        player_id = 1
        for item in data:
            player_name = item['name']
            team = item['team']
            overall = item['overallAttribute']
            price = overall * 1.25
            
            # Prepare the data to be written
            record = {
                "id": player_id,
                "overall": overall,
                "price": price,
                "player": player_name,
                "team": team
            }
            
            # Write the record to the CSV file
            writer.writerow(record)
            
            # Increment the player_id for the next record
            player_id += 1

# Write the JSON data to a CSV file
write_to_csv(data, 'player_values.csv')
