
# speedup versus number of threads
# I guess this is "Speed up over serial partition"

import matplotlib.pyplot as plt
import numpy as np
inPlace = [ ( 1, 0.520833), ( 2, 0.78125), ( 3, 0.694444), ( 4, 0.892857), ( 5, 0.892857), ( 6, 0.806452), ( 7, 0.833333), ( 8, 0.78125), ( 9, 0.735294), ( 10, 0.757576), ( 11, 0.714286), ( 12, 0.735294), ( 13, 0.675676), ( 14, 0.714286), ( 15, 0.694444), ( 16, 0.641026), ( 17, 0.609756), ( 18, 0.510204) ]
inPlacePrefixSum = [ (1, 0.462963), ( 2, 0.675676), ( 3, 0.892857), ( 4, 0.757576), ( 5, 0.833333), ( 6, 0.78125), ( 7, 0.78125), ( 8, 0.625), ( 9, 0.806452), ( 10, 0.757576), ( 11, 0.78125), ( 12, 0.862069), ( 13, 0.568182), ( 14, 0.641026), ( 15, 0.609756), ( 16, 0.735294), ( 17, 0.757576), ( 18, 0.714286) ] 
outOfPlace = [ ( 1, 0.367647), ( 2, 0.5), ( 3, 0.520833), ( 4, 0.531915), ( 5, 0.510204), ( 6, 0.5), ( 7, 0.531915), ( 8, 0.490196), ( 9, 0.462963), ( 10, 0.490196), ( 11, 0.510204), ( 12, 0.5), ( 13, 0.520833), ( 14, 0.510204), ( 15, 0.5), ( 16, 0.462963), ( 17, 0.446429), ( 18, 0.454545) ]
highSpan = [ ( 1, 0.833333), ( 2, 0.757576), ( 3, 1.25), ( 4, 1.25), ( 5, 1.04167), ( 6, 1.25), ( 7, 1.13636), ( 8, 1.04167), ( 9, 1.04167), ( 10, 1.04167), ( 11, 1), ( 12, 1), ( 13, 1), ( 14, 1), ( 15, 0.862069), ( 16, 0.833333), ( 17, 0.641026), ( 18, 0.675676) ]
cacheFriendly = [ ( 1, 0.568182), ( 2, 0.555556), ( 3, 0.5), ( 4, 0.480769), ( 5, 0.555556), ( 6, 0.609756), ( 7, 0.543478), ( 8, 0.581395), ( 9, 0.510204), ( 10, 0.446429), ( 11, 0.431034), ( 12, 0.423729), ( 13, 0.568182), ( 14, 0.568182), ( 15, 0.555556), ( 16, 0.531915), ( 17, 0.555556), ( 18, 0.543478) ]

plt.plot([xi[0] for xi in inPlace], [xi[1] for xi in inPlace])
plt.plot([xi[0] for xi in inPlacePrefixSum], [xi[1] for xi in inPlacePrefixSum])
plt.plot([xi[0] for xi in outOfPlace], [xi[1] for xi in outOfPlace])
plt.plot([xi[0] for xi in highSpan], [xi[1] for xi in highSpan])
plt.plot([xi[0] for xi in cacheFriendly], [xi[1] for xi in cacheFriendly])
plt.show()


