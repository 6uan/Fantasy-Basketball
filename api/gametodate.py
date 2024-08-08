from nba_api.stats.endpoints import boxscoresummaryv2

game_id = '0021900001'  # Replace with your game_id

def get_game_date(game_id):
    try:
        # Fetch boxscore summary for the given game_id
        boxscore_summary = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id)
        # The date of the game can be found in the game_summary data
        game_summary = boxscore_summary.game_summary.get_dict()
        game_date = game_summary['data'][0][0]  # Adjust the index based on the actual data structure
        return game_date
    except Exception as e:
        print(f"Error fetching game date: {e}")
        return None

# Example usage
game_date = get_game_date(game_id)
if game_date:
    print(f"The date of the game with ID {game_id} is {game_date}")
else:
    print("Game date could not be retrieved.")
