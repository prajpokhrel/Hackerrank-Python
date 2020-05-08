import numpy as np

integers = map(int, input().split())
dimensions = list()
for values in integers:
    dimensions.append(values)
shape = tuple(dimensions)
print(np.zeros(shape, dtype = np.int))
print(np.ones(shape, dtype = np.int))





