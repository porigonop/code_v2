import numpy as np
import csv
from pprint import pprint
import matplotlib.pyplot as plt 
import sklearn.linear_model as sk
from sklearn.linear_model import RANSACRegressor

#opening csv file 
fileh = open('exam_data.csv', 'rb')
file_ = csv.reader(fileh, delimiter = ' ', skipinitialspace = True)

# Je ne sais plus comment surprimer les k premiere lignes, j'utilise donc
# une methode maison
age = []
bloodpressure = []
testing = False
for row in file_:
	if testing:
		age.append(int(row[2]))
		bloodpressure.append(int(row[3]))
	if row[0] == "Systolic": 	# dernier mot avant les donnees a \
								#proprement parler
		testing = True
#closing file
fileh.close()

age = np.array(age)
bloodpressure = np.array(bloodpressure)

plt.hist(age)
plt.title("age")
plt.show()
		
plt.hist(bloodpressure)
plt.title("blood pressure")
plt.show()

plt.scatter(age, bloodpressure)
plt.title("blood pressure = f(age)")
plt.show()

#reshaping data
age = age.reshape(len(age), 1)
bloodpressure = bloodpressure.reshape(len(bloodpressure), 1)

#creating reglin object
reglin = sk.LinearRegression()

#fit object
reglin.fit(age, bloodpressure)

#printing y = ax + b
print("y = " + \
	str(reglin.coef_[0][0]) + \
	"x + " + \
	str(reglin.intercept_[0]))

#printing R^2 = k
print("R^2 = " + \
		str(reglin.score(age, bloodpressure)))

#creating mean
pression_predicted = np.array([reglin.coef_[0][0] * i + reglin.intercept_[0] for i in age])


plt.scatter(age, bloodpressure - pression_predicted)
plt.title("residues = f(age)")
plt.show()

plt.hist(bloodpressure - pression_predicted)
plt.title("residues")
plt.show()

#creating object reglin ransac mod
ransac = RANSACRegressor()
ransac.fit(age, bloodpressure)

#selection of the wanted data with mask
inlier_age = age[ransac.inlier_mask_]
inlier_bloodpressure = age[ransac.inlier_mask_]

#generating the new reglin
reglinlier = sk.LinearRegression()
reglinlier.fit(inlier_age, inlier_bloodpressure)

#new R^2
print("R^2 = " + str(reglinlier.score(inlier_age, inlier_bloodpressure)))









