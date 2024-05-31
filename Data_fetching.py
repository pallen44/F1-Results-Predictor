import fastf1 as ff1
import numpy as np
import pandas as pd
from fastf1.core import SessionResults

# Stores data in cache folder to decrease API hit rate
ff1.Cache.enable_cache('../cache_directory')

## Initial data fetching position for all drivers
def fetch_race_results(year, round_number):
  session = ff1.get_session(year, round_number, 'R')
  session.load()
  results = session.results
  drivers = results['Abbreviation']
  # print(drivers)
  # results_df = pd.DataFrame(results)
  return drivers  

def total_rounds_last_year(year):
  schedule = ff1.get_event_schedule(year, include_testing=False)
  
  num_rounds = schedule['RoundNumber'].nunique()
  return num_rounds

race_data = []
current_year = int(input("Enter current season: "))
current_round = int(input("Last race number: "))

i = j = 0
for i in range(10):
  year = current_year
  round_number = current_round - i
  if round_number <= 0: # if the there is less than 10 races in current season
    year -= 1
    last_year_round_number = total_rounds_last_year(year) - j
    j += 1
    race_data.append(fetch_race_results(year, last_year_round_number))
  else: 
    race_data.append(fetch_race_results(year, round_number))

print(race_data)