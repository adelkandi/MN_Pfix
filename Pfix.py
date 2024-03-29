

import numpy as np 
from matplotlib import pyplot as plt
import matplotlib as plot 
from math import * 


def f(x):
    x**3 - (11/6)*(x**2)+x-1/6 # the function f(x) that we need find there racine x that is solution 

def g(x):
    3*x**2 - (11/6)*2*x + 1 # g(x) the derivative of the f function 

i = 1 # init the iteration to 1
x = 0
x1 = None   #Initialize x1 to none no value 
eps = float(input("The Error Value:"))
def PFix(x,eps):
    while abs(x1-x) > eps:
        x1 = g(x)       # change the value from x1 to g(x ) untile find out the racine of the function f(x)
        i = i+1
    
# New update :
result = PFix(x,eps) # 
print("The Solution of the function is: ",result)
print("The Nuber of iteration is: ",i) # print number of iteration  

# plot the functions graph :
x = np.linspace(1,1,100)
y = x**3 - (11/6)*(x**2)+x-1/6 # The function f(x) we will plot 
plt.subplot(1,1,1)
plt.plot(x ,y)            # Plot the function graph 
plt.xlabel("axe x")       
plt.ylabel("axe y")

# Plot the g(x) Function Graph 
plt.subplot(2,1)
xg = np.linspace(1,1,100)
yg =  3*x**2 - (11/6)*2*x + 1  # g(x) Function 
plt.plot(xg ,yg)            # Plot the function graph 
plt.xlabel("axe x")       
plt.ylabel("axe y")

# Plot the g'(x) Graph 
xg1 = np.linspace(1,1,100)
yg1 =  6*x - (11/6)*6    # The g'(x) Function 
plt.plot(xg1 ,yg1)            # Plot the function graph 
plt.xlabel("axe x")       
plt.ylabel("axe y")
plt.show()








