import plotly.express as px
from random import randint
from collections import defaultdict

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
die_1 = Die()
die_2 = Die()
results = {}

for i in range(5000000):
    result = die_1.roll() + die_2.roll()
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

dict_values = list(results.values())
x_values = range(1, 12)

# Visualize the results
title = "Resulst of rolling one D6 100 times"
lables = {'x': 'Result', 'y': 'Frequency'}
fig = px.bar(x=x_values, y=dict_values, title=title, labels=lables)
fig.show()

# for key, value in results.items():
#     print(f"{key} is {value}% percent")
