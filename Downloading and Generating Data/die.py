from random import randint
from collections import defaultdict

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
hello_mfs = Die()
results = {}

for i in range(100):
    result = hello_mfs.roll()
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

for key, value in results.items():
    print(f"{key} is {value}% percent")
