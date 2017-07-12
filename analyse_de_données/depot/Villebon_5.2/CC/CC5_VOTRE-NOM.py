import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model



# QUESTION 1
data = np.loadtxt()           # completer
F =                           # 1ere colonne
T =                           # 2eme colonne

# QUESTION 2
plt.                          # afficher le nuage de point
plt.show()

# QUESTION 3
F = F.reshape(21,1)			 # pour scikit-learn
T = T.reshape(21,1)

regr =                       # instancier le modèle de regression
                             # fit du modèle

print                        # print des coefficients de la droite

# QUESTION 4
print                        # coefficient R2

residus = 
                             # histogramme des résidus
plt.show()
