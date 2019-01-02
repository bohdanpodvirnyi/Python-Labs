import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


random_array = np.random.rand(317, 21)
print(random_array)

value = float(input())
array_of_closest_values = []
for array in random_array:
    array_of_closest_values.append(find_nearest(array, value))

print(find_nearest(array_of_closest_values, value))
