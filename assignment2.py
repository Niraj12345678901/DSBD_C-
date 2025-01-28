import pandas as pd
# Runs scored by players in different matches
data = {
    "Match 1": [45, 60, 20, 80, 55],
    "Match 2": [30, 50, 40, 90, 65],
    "Match 3": [70, 20, 35, 60, 40],
    "Match 4": [25, 45, 15, 100, 75],
}

players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]
performance = pd.DataFrame(data, index = players)

# Display the first three rows of the performance DataFrame.
first_three_rows = performance.head(3)
print(first_three_rows)

# Get the number of players and matches recorded in the DataFrame
num_players, num_matches = performance.shape
print(f"Number of players: {num_players} \nNumber of matches: {num_matches}")

# List the match names and player names.
match_names = performance.columns.tolist()
player_names = performance.index.tolist()
print(f"Matches: {match_names}")
print(f"Players: {player_names}")

# Display the data type of the elements in the DataFrame.
print(performance.dtypes)

# Check if there are any missing values in the DataFrame.
print(performance.isnull().sum().sum())

# Retrieve the scores of "Player 4" across all matches.
player_4_scores = performance.loc["Player 4"]
print(player_4_scores)

# Extract the scores of all players in "Match 2".
match_2_scores = performance["Match 2"]
print(match_2_scores)

# Retrieve the scores of "Player 1" and "Player 3" for "Match 1" and "Match 4".  
scores_p1_p3 = performance.loc[["Player 1", "Player 3"], ["Match 1", "Match 4"]]
print(scores_p1_p3)

# Slice the DataFrame to get the first 3 players and the first 2 matches.
sliced_data = performance.iloc[:3, :2]
print(sliced_data)

# Find the score of "Player 5" in "Match 3" using .loc or .iloc.
player_5_match_3 = performance.loc["Player 5", "Match 3"]
print(player_5_match_3)

# Update the score of "Player 2" in "Match 4" to 50.
performance.loc["Player 2", "Match 4"] = 50
print(performance)

# Add a new player, "Player 6", with scores [50, 40, 60, 70] in all matches.
performance.loc["Player 6"] = [50, 40, 60, 70]
print(performance)

# Add 10 bonus runs to all scores in the DataFrame.
performance += 10
print(performance)

# Deduct 5 runs from the scores of "Player 3" in all matches.
performance.loc["Player 3"] -= 5
print(performance)

# Calculate the percentage contribution of each player’s score in a match, assuming the maximum possible score in each match is 120 runs.
percentage_contribution = (performance / 120) * 100
print(percentage_contribution)

# Calculate the total runs scored by each player across all matches.
total_runs_per_player = performance.sum(axis=1)
print(total_runs_per_player)

# Determine the total runs scored in each match.
total_runs_per_match = performance.sum(axis=0)
print(total_runs_per_match)

# Find the player with the highest total runs.
max_runs_player = total_runs_per_player.idxmax()
print(f"Player with highest total runs: {max_runs_player}")

# Identify the match with the lowest total runs.
min_runs_match = total_runs_per_match.idxmin()
print(f"Match with lowest total runs: {min_runs_match}")

# Compute the average runs scored by each player across all matches.
average_runs_per_player = performance.mean(axis = 1)
print(average_runs_per_player)

# Add a new column called "Total Runs" that displays the total runs scored by each player.
performance["Total Runs"] = total_runs_per_player
print(performance)

# Sort the DataFrame by the "Total Runs" column in descending order.
performance_sorted = performance.sort_values("Total Runs", ascending = False)
print(performance_sorted)

# Filter the players who scored a total of more than 200 runs.
players_above_200 = performance[performance["Total Runs"] > 200]
print(players_above_200)




