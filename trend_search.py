import sys
import os
from pytrends.request import TrendReq
from datetime import datetime

pytrends = TrendReq(hl='en-US', tz=360)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
str_current_datetime = str(current_datetime)
file_name = str_current_datetime+" Trend Search.txt"
output_file_path = os.path.join(desktop_path, file_name)

sys.stdout = open(output_file_path, 'w')
countries = ['united_states', 'india','united_kingdom']

def trending_searches(country):
    data = pytrends.trending_searches(country)
    print(data.head(5))

for country in countries:
    print(country)
    print('')
    trending_searches(country)
    print('')


sys.stdout.close()

sys.stdout = sys.__stdout__