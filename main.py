"""
Weather Forecast
"""
### Reading CSV using file handling takes 8 lines of code and returns a non-formatted data from the csv file
### Whereas pandas consist only three lines, pandas are more efficient in data analysis and reading csv

import pandas as pd
data = pd.read_csv('weather_data.csv')

# Get Column Temperature which is a Data Series object
temp_list = data['temp'].to_list()

# Get the Average Temperature the Traditional way and using Pandas, see the comparison:
#print(f"Average Temperature: {round(sum(temp_list)/len(temp_list),2)}")
print(data['temp'].mean()) # Average Temperature
print(f"Maximum Temperature Value: {data['temp'].max()}") # Maximum Temperature Value

# Get Column names
print(data['condition']) # Instead of this
print(data.condition) # Use this


#
