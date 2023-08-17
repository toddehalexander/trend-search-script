import sys
import os
from pytrends.request import TrendReq
from datetime import datetime

#establishing connection with pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Specify the file path on your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

#Assigning the name of the txt file
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
str_current_datetime = str(current_datetime)
file_name = str_current_datetime+" Trend Search.txt"
output_file_path = os.path.join(desktop_path, file_name)

# Redirecting the standard output to the text file
sys.stdout = open(output_file_path, 'w')

#List of contries, Caps sensitive which pytrends uses
countries = ['united_states', 'india','united_kingdom']

#function to get the 4 most trending searches of specifed countries
def trending_searches(country):
    data = pytrends.trending_searches(country)
    print(data.head(5))

#for loop to print trending searchs for each country
for country in countries:
    print(country)
    print('')
    trending_searches(country)
    print('')

# Closing the text file
sys.stdout.close()

# Resetting the standard output
sys.stdout = sys.__stdout__