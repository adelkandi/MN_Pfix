import math 



def f(x):
    x**3 - (11/6)*(x**2)+x-1/6 # the function f(x) that we need find there racine x that is solution 

def g(x):
    3*x**2 - (11/6)*2*x + 1 # g(x) the derivative of the f function 


x = 0 
x1 = None   #Initialize x1 to none no value 
eps = input("Give the Epselon Value:")
while abs(x1-x) > eps:
    x1 = g(x)       # change the value from x1 to g(x ) untile find out the racine of the function f(x)
    i = i+1
    
print(x1)
print(i) # print number of iteration  
