##################
# J   Plumitallo #
# comp. simp.    #
##################

import numpy as np
import time
from matplotlib import pyplot as plt

def f(x):

    return np.exp(-x**2)

a=0
b=5
m = 8
x = np.linspace(a,b,2*m+1)

x_odd = x[1:2*m:2]
x_even = x[2:2*m:2]

composite_simpson = f(a)+f(b)+4*(np.sum(f(x_odd)))+2*(np.sum(f(x_even)))
composite_simpson *= float(b-a)/((len(x_odd)+len(x_even)+1)*3)

print composite_simpson
