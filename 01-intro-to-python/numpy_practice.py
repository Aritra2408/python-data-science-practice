"""Intro to Python - NumPy practice.

Covers: arrays vs lists, element-wise math, one-type rule, subsetting,
2D arrays, basic statistics, and generating random data.
"""
import numpy as np

# 1. Why NumPy? Lists can't do element-wise math -------------------------
height = [1.73, 1.68, 1.71, 1.89, 1.79]   # metres
weight = [65.4, 59.2, 63.6, 88.4, 68.7]   # kg

try:
    weight / height ** 2
except TypeError as e:
    print("List math fails:", e)

# 2. NumPy arrays: calculations over whole arrays ------------------------
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
print("BMI:", np.round(bmi, 2))

# 3. Remarks: one data type only, and different behaviour ----------------
print(np.array([1.0, "is", True]))        # everything coerced to strings
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
print(python_list + python_list)          # [1, 2, 3, 1, 2, 3]  (concatenates)
print(numpy_array + numpy_array)          # [2 4 6]             (adds)

# 4. Subsetting 1D arrays -------------------------------------------------
print("Second BMI:", bmi[1])
print("BMI > 23 mask:", bmi > 23)
print("BMI values > 23:", bmi[bmi > 23])

# 5. 2D arrays ------------------------------------------------------------
np_2d = np.array([height, weight])
print(np_2d)
print("type:", type(np_2d), "| shape:", np_2d.shape)   # (2, 5)

# 6. Subsetting 2D arrays -------------------------------------------------
print("First row:", np_2d[0])
print("Row 0, col 2:", np_2d[0, 2])                    # same as np_2d[0][2]
print("All rows, cols 1-2:\n", np_2d[:, 1:3])
print("Second row:", np_2d[1, :])

# 7. Basic statistics and 8. generating data ------------------------------
np.random.seed(42)   # reproducible results
heights = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weights = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((heights, weights))
print("city shape:", np_city.shape)

print("mean height:  ", np.mean(np_city[:, 0]))
print("median height:", np.median(np_city[:, 0]))
print("std height:   ", np.std(np_city[:, 0]))
print("correlation:\n", np.corrcoef(np_city[:, 0], np_city[:, 1]))
