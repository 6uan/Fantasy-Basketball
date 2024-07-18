from nba_api.stats.endpoints import playercareerstats
from pandas import DataFrame

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
example = career.get_data_frames()[0]
print(example)