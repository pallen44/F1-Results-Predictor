'''Module which fetches all data for drivers and finishing positions of last ten races'''
import logging
import fastf1 as ff1
from fastf1 import RateLimitExceededError

class RaceDataFetcher:
    '''Functions to hit API and gather all of the race data'''
    def __init__(self, cache_dir='../cache_directory'):
        ff1.Cache.enable_cache(cache_dir)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def fetch_race_results(self, season, race_number):
        '''Initial data fetching position for all drivers'''
        self.logger.info("fetch_race_results was called")
        try:
            session = ff1.get_session(season, race_number, 'R')
            session.load()
            drivers = session.results[['DriverNumber', 'Position','Abbreviation']]
            return drivers
        except RateLimitExceededError as e:
            self.logger.error("Error fetching race results for %d, race %d: %s",
                              season, race_number, e)
            raise

    def total_rounds_last_year(self, previous_season):
        '''Gets the count of total rounds in last season'''
        self.logger.info("total_rounds_last_year called")
        try:
            schedule = ff1.get_event_schedule(previous_season, include_testing=False)
            num_rounds = schedule['RoundNumber'].nunique()
            return num_rounds
        except RateLimitExceededError as e:
            self.logger.error("Error getting race schedule last season: %d : %s",
                              previous_season, e)
            raise

    def get_last_ten_races(self, current_year, current_round):
        '''Gets data for last ten races'''
        self.logger.info("get_last_ten_races was called")
        race_data = []
        rounds_to_fetch = 10

        while rounds_to_fetch > 0:
            while current_round > 0 and rounds_to_fetch > 0:
                race_data.append(self.fetch_race_results(current_year, current_round))
                current_round -= 1
                rounds_to_fetch -= 1
            if current_round == 0: # if there is less than 10 races in the current season
                current_year -= 1
                current_round = self.total_rounds_last_year(current_year)

        self.logger.info('Finished fetching all data')
        return race_data
    