import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# QUESTION 1
data = np.loadtxt('CC6_data.csv', delimiter = ";")    
T, F = data[:,1], data[:,2]

# QUESTION 2
plt.scatter(T,F)     
plt.xlabel('Celsius')
plt.ylabel('Fahrenheit')                      
plt.show()


# QUESTION 3
F = F.reshape(21,1)			                 
T = T.reshape(21,1)

regr =  linear_model.LinearRegression()    
regr.fit(T,F)                               

print "valeurs des coefficients a et b de la droite"
print regr.coef_, regr.intercept_
np.testing.assert_approx_equal(regr.coef_, 1.8, significant=1) 
np.testing.assert_approx_equal(regr.intercept_, 32, significant=1)

# QUESTION 4
print "coefficient R2 :", regr.score(T,F)      

residus = F-regr.predict(T)                 
plt.scatter (T,residus)
plt.xlabel('Celsius')
plt.title('residus')
plt.show()
