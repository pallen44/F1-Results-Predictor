'''Preprocessing Data File'''
import logging
import pandas as pd

class Preprocessing:
    '''Class for preprocessing data before sending to model'''
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def check_for_nullvalues(self, df):
        '''Returns number of missing values in dataset if any'''
        self.logger.info("check_for_nullvalues was called")
        if df.isnull().values.any() :
            null_values = df.isnull().sum()
            self.logger.warning("Found null values: \n %s", null_values)
            return null_values

        self.logger.info("No null values!")
        return print("No null values!")

    def avg_race_position(self, race_datadf):
        '''Calculates the avg race finish for each driver and adds to df'''
        if race_datadf.empty:
            self.logger.error("The input DataFrame is empty!")
            raise ValueError("The input DataFrame is empty!")

        try:
            # Group by driver abbreviation to calculate average position
            avg_positions = race_datadf.groupby('Abbreviation')['Position'].mean().reset_index()
            avg_positions.columns = ['Abbreviation', 'Average_Position']
        except Exception as e:
            self.logger.error("Error calculating average positions: %s", e)
            raise

        try:
            # Merge the average position back into the original dataframe
            race_datadf = race_datadf.merge(avg_positions, on='Abbreviation', how='left')
        except Exception as e:
            self.logger.error("Error merging average positions into DataFrame: %s", e)
            raise

        return race_datadf

    def preprocess_data(self, race_data):
        '''Calls other functions within this class and processes data'''
        try:
            # Convert list of DataFrames to a single DataFrame
            race_data_df = pd.concat(race_data, ignore_index=True)
            race_data_df = race_data_df.sort_values('DriverNumber')
        except Exception as e:
            self.logger.error("Error concatenating race data: %s", e)
            raise

        if race_data_df.empty:
            self.logger.error("The concatenated DataFrame is empty!")
            raise ValueError("The concatenated DataFrame is empty!")

        # Check for null values
        self.logger.info(self.check_for_nullvalues(race_data_df))

        # Calculate average race position
        race_data_df = self.avg_race_position(race_data_df)

        # Log the final shape of the DataFrame
        self.logger.info("Final DataFrame shape: %s", race_data_df.shape)

        return race_data_df
