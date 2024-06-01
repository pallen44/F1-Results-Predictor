'''Main File'''
from data_fetching import RaceDataFetcher

def main():
    '''Main function'''
    current_year = int(input("Enter current season: "))
    current_round = int(input("Last race number: "))
    fetcher = RaceDataFetcher()
    race_data = fetcher.get_last_ten_races(current_year, current_round)
    print(race_data)

if __name__ == "__main__":
    main()
