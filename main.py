"""
Weather Forecast
"""
### Reading CSV using file handling takes 8 lines of code and returns a non-formatted data from the csv file
### Whereas pandas consist only three lines, pandas are more efficient in data analysis and reading csv

import pandas as pd
# data = pd.read_csv('weather_data.csv')

# Get Column Temperature which is a Data Series object
# temp_list = data['temp'].to_list()

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
# monday = data[data.day=='Monday']
# print(monday)

# Get monday's temperature that is in Celsius then convert it into Fahrenheit
# monday_temperature = monday.temp[0]
# print(f"Monday's Temperature in Celsius: {monday_temperature} Degrees Celsius\nMonday's Temperature in Fahrenheit: {((9/5)*monday_temperature)+32} Degrees Fahrenheit")

# Create a dataframe from scratch
# student_data = {
#     'students': ['Anna', 'John', 'Ezekiel', 'Joshua'],
#     'scores': [96,97,88,86],
# }
# new_data = pd.DataFrame(student_data)
# print(new_data)

# Convert new data frame to csv
# new_data.to_csv('new_data.csv')

"""
Goal: By using data analysis on the dataset of the squirrel data, extract how many squirrels are there base
on their fur colors (Black, Cinnamon, Red)
"""
squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

cinnamon_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color']== 'Cinnamon'])
black_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color']== 'Black'])
gray_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color']== 'Gray'])

squirrel_fur_count = {
    'Primary Fur Color': ['Black', 'Gray', 'Cinnamon'],
    'Count': [black_squirrels,gray_squirrels,cinnamon_squirrels],
}
squirrel_fur_count_df = pd.DataFrame(squirrel_fur_count) # Convert Dictionary to DataFrame
squirrel_fur_count_df.to_csv('squirrel_fur_count.csv') # Convert DataFrame to CSV



