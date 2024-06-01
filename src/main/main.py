'''Main File'''
from data_fetching import RaceDataFetcher
import pandas as pd

def main():
    '''Main function'''
    current_year = int(input("Enter current season: "))
    current_round = int(input("Last race number: "))
    fetcher = RaceDataFetcher()
    race_data = fetcher.get_last_ten_races(current_year, current_round)
    race_data_df = pd.concat(race_data)
    print(race_data_df)

if __name__ == "__main__":
    main()
