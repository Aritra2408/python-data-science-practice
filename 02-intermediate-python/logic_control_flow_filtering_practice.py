"""Intermediate Python - Logic, Control Flow and Filtering practice.

Covers: comparison operators, comparing NumPy arrays, and/or/not,
np.logical_and/or/not, if/elif/else, and filtering Pandas DataFrames
with boolean Series.
"""
import numpy as np
import pandas as pd

# 1. Equality and inequality ---------------------------------------------
print(True == False)          # False
print(-5 * 15 != 75)          # True
print("pyscript" == "PyScript")  # False (case-sensitive)
print(True == 1)              # True (bool is a special kind of int)

# 2. Greater than / less than --------------------------------------------
x = -3 * 6
print(x >= -10)               # False
print("test" <= "test")       # True (strings compare alphabetically)
print(True > False)           # True

# 3. Comparing NumPy arrays ----------------------------------------------
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house >= 18)             # [ True  True False False]
print(my_house < your_house)      # [False  True  True False]

# 4. and, or, not --------------------------------------------------------
my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen > 10 and my_kitchen < 18)       # False
print(my_kitchen < 14 or my_kitchen > 17)        # True
print(my_kitchen * 2 < your_kitchen * 3)         # True

# `not` binds tighter than `and` / `or`
a, b = 8, 9
print(not (not (a < 3) and not (b > 14 or b > 10)))  # False

# 5. Boolean operators with NumPy ----------------------------------------
print(np.logical_or(my_house > 18.5, my_house < 10))   # [False  True False  True]
print(np.logical_and(my_house < 11, your_house < 11))  # [False False False  True]

# 6. if / elif / else ----------------------------------------------------
room = "bed"
area = 14.0

if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

if area > 15:
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else:
    print("pretty small.")

# 7. Filtering Pandas DataFrames -----------------------------------------
# Same data as the DataCamp cars.csv, built inline so the script runs anywhere.
cars = pd.DataFrame(
    {
        "cars_per_cap": [809, 731, 588, 18, 200, 70, 45],
        "country": ["United States", "Australia", "Japan", "India",
                    "Russia", "Morocco", "Egypt"],
        "drives_right": [True, False, False, False, True, True, True],
    },
    index=["US", "AUS", "JPN", "IN", "RU", "MOR", "EG"],
)

# Boolean Series -> subset rows
dr = cars["drives_right"]
sel = cars[dr]
print(sel)

# One-liner
sel = cars[cars["drives_right"]]

# Countries with more than 500 cars per 1000 people
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]
print(car_maniac)

# Between 100 and 500 (np.logical_and works on Series too)
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium)
