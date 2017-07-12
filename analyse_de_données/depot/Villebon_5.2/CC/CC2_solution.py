import numpy as np

params=(5,3)
x = 10*np.random.random(100)
y = params[0] + params[1]*x + np.random.normal(size=len(x))


def moyenne(v):
    return sum(v)/len(v)

def produit_scalaire(x,y):
    return sum(p*q for p,q in zip(x, y))

def variance(x):
    return 1./(len(x)-1)*sum(np.square(x-moyenne(x)))

def covariance(x,y):
    return 1./(len(x)-1)*produit_scalaire(x-moyenne(x),y-moyenne(y))
    
def linear_parameters(x,y):
    theta_1 = covariance(x,y)/variance(x)
    theta_0 = moyenne(y)-theta_1*moyenne(x)
    return theta_0, theta_1

print linear_parameters(x,y)