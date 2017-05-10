##################
# J   Plumitallo #
# adap simp      #
##################

import numpy as np
import matplotlib as plt

#global variables
fc = 0
nodes = []

#function definition
def z(x):

    return np.exp(-x**2)

#simpson's rule funciton definition
def simpsons_rule(f,a,b):
    
    c = (a+b) / 2.000
    h3 = abs(b-a) / 6.0
    return h3*(f(a) + 4.0*f(c) + f(b))

#recursive adaptive simpson's rule function definition
def recursive_asr(f,a,b,eps,whole):

    c = (a+b) / 2.0
    left = simpsons_rule(f,a,c)
    right = simpsons_rule(f,c,b)
    
    if abs(left + right - whole) <= 15*eps:
        
        return left + right + (left + right - whole)/15.0
   
    nodes.append([a,b,c])

    global fc
    fc+=1

    return recursive_asr(f,a,c,eps/2.0,left) + recursive_asr(f,c,b,eps/2.0,right)

#adaptive simpson's rule function definition
def adaptive_simpsons_rule(f,a,b,eps):

    return recursive_asr(f,a,b,eps,simpsons_rule(f,a,b))

print (adaptive_simpsons_rule(z,0,5,.0000000001))

print 'Number of recursive function calls: ' , fc
nodes = np.unique(nodes)
print 'Nodes accessed: ' , nodes
