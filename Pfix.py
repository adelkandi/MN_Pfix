import math 



def f(x):
    x**3 - (11/6)*(x**2)+x-1/6

def g(x):
    3*x**2 - (11/6)*2*x + 1 # g(x) the derivative of the f function 

x = 0 
eps = input("Give the Epselon Value:")
while abs(x1-x) > eps:
    x1 = g(x)
    i = i+1

print(i)
