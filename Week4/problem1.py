#Input in format {+/-}coefficient*term and seperate with spaces, e.g. 4*x^2 +2*x

import numpy as np

poly_1 = input("Type the first polynomial: ")
poly_2 = input("Type the second polynomial: ")

poly_1 = [int(x) for x in poly_1.split(' ')]
poly_2 = [int(x) for x in poly_2.split(' ')]

p1 = np.poly1d(poly_1)
p2 = np.poly1d(poly_2)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
