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
# print(data['temp'].mean()) # Average Temperature
# print(f"Maximum Temperature Value: {data['temp'].max()}") # Maximum Temperature Value
#
# # Get Column names
# print(data['condition']) # Instead of this
# print(data.condition) # Use this

# Get Row Data where => it has Temperature as the Maximum Value
# print(data[data.temp == data.temp.max()])

# Get Row Data for One Single Day
monday = data[data.day=='Monday']
print(monday)

# Get monday's temperature that is in Celsius then convert it into Fahrenheit
monday_temperature = monday.temp[0]
print(f"Monday's Temperature in Celsius: {monday_temperature} Degrees Celsius\nMonday's Temperature in Fahrenheit: {((9/5)*monday_temperature)+32} Degrees Fahrenheit")

# Create a dataframe from scratch
student_data = {
    'students': ['Anna', 'John', 'Ezekiel', 'Joshua'],
    'scores': [96,97,88,86],
}
new_data = pd.DataFrame(student_data)
print(new_data)

# Convert new data frame to csv
# new_data.to_csv('new_data.csv')


