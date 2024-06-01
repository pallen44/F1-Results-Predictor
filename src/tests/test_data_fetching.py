'''Data Fetching Test File'''
from unittest.mock import MagicMock, patch
import sys
import pytest
from data_fetching import RaceDataFetcher

sys.path.append("../main")

class TestRaceDataFetcher:
    '''Class to test RaceDataFetcher Class'''

    @pytest.fixture(scope="module")
    def fetcher(self):
        '''Creates a fixture of the testing class'''
        return RaceDataFetcher()

    def test_fetcher_initialization(self, fetcher):
        '''Tests Initialization of the RaceDataFetcher class'''
        assert fetcher is not None
        assert fetcher.logger.name == 'RaceDataFetcher'

    @patch('main.data_fetching.ff1.get_session')
    def test_fetch_race_results(self, mock_get_session, fetcher):
        '''Tests that fetch data hits api and returns data'''
        season = 2023
        race_number = 1

        mock_session = MagicMock()
        mock_session.results = {'Abbreviation' : ['VER', 'PER', 'ALO']}
        mock_get_session.return_value = mock_session

        drivers = fetcher.fetch_race_results(season, race_number)
        assert drivers == ['VER', 'PER', 'ALO']
        mock_get_session.assert_called_once_with(season, race_number, 'R')


    def test_total_rounds_last_year(self, fetcher):
        '''Tests that total rounds is returned'''
        # Implement your test here

    def test_get_last_ten_races(self, fetcher):
        '''Tests that the last ten races are gotten'''
        # Implement your test here
