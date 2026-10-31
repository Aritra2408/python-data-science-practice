"""Intro to Python (DataCamp) - Dictionaries and Pandas practice.

Covers: dictionaries vs lists, immutable keys, DataFrames from a
dictionary, and selecting with [], loc and iloc.
"""
import pandas as pd

# Dictionaries: look up by key instead of index
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]
print("List way:", pop[countries.index("albania")])
world = dict(zip(countries, pop))
print("Dict way:", world["albania"])

world["albania"] = 2.81            # update
world["sealand"] = 0.000027        # add
print(world)

# Keys must be immutable (a list as a key raises TypeError)
try:
    {["just", "to", "test"]: "value"}
except TypeError as e:
    print("Error:", e)

# DataFrame from a dictionary
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}
brics = pd.DataFrame(data)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Column access
print(brics["country"])                    # Series
print(brics[["country", "capital"]])       # DataFrame

# Row access with slicing
print(brics[1:4])

# loc: label-based
print(brics.loc["RU"])                     # Series
print(brics.loc[["RU", "IN", "CH"]])
print(brics.loc[:, ["country", "capital"]])
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])

# iloc: position-based
print(brics.iloc[[1, 2, 3]])
print(brics.iloc[:, [0, 1]])
print(brics.iloc[[1, 2, 3], [0, 1]])
