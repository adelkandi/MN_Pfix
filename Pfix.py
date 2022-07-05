
from pdb import line_prefix
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib as plot 



def f(x):
    x**3 - (11/6)*(x**2)+x-1/6 # the function f(x) that we need find there racine x that is solution 

def g(x):
    3*x**2 - (11/6)*2*x + 1 # g(x) the derivative of the f function 


x = 0 
x1 = None   #Initialize x1 to none no value 
eps = 10**-(int(input("Give the Epselon power:10**-")))
while abs(x1-x) > eps:
    x1 = g(x)       # change the value from x1 to g(x ) untile find out the racine of the function f(x)
    i = i+1
    
print(x1)
print(i) # print number of iteration  

# plot the functions graph :
x = np.linspace(1,1,100)
y = x**3 - (11/6)*(x**2)+x-1/6 # The function we will plot 
plt.subplot(3,1,1)
plt.plot(x ,y)
plt.xlabel("axe x")
plt.ylabel("axe y")
plt.show()








