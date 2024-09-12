from pathlib import Path 
import csv 

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
head_row = next(reader)

print(head_row)