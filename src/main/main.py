'''Main File'''
from data_fetching import RaceDataFetcher
from preprocessing import Preprocessing
from model_training import ModelTraining

def main():
    '''Main function'''
    current_year = int(input("Enter current season: "))
    current_round = int(input("Last race number: "))

    # Fetch race data
    fetcher = RaceDataFetcher()
    race_data = fetcher.get_last_ten_races(current_year, current_round)

    # Preprocess data
    preprocessor = Preprocessing()
    race_data_df = preprocessor.preprocess_data(race_data)
    print(race_data_df)

    # Train Model
    trainer = ModelTraining()
    trained_model = trainer.train_model(race_data_df)
    print(trained_model)


if __name__ == "__main__":
    main()
