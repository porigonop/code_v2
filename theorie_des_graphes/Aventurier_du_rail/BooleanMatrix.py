#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class BooleanMatrix():
        def __init__(self, coefficients):
                if type(coefficients) != list:
                        raise TypeError("l'argument donnÃƒÂ© n'est pas une liste")

                longueur = len(coefficients)

                for i in range(longueur):
                        if type(coefficients[i]) != list:
                                raise TypeError("l'argument donnÃƒÂ© n'est pas une liste de liste")
            
                        if len(coefficients[i]) != longueur:
                                raise TypeError("l'argument donnÃƒÂ© n'est pas une matrice carrÃƒÂ©e")
            
                        for j in range(longueur):
                                if coefficients[i][j] != 0 and coefficients[i][j] != 1:
                                        raise ValueError("les coefficients doivent ÃƒÂªtre des 0 ou "
                                     + "des 1")

                self.coefficients = coefficients
         
        def multiply(self, matrice):
                
                if type(matrice) != type(self):
                        raise TypeError("La matrice ÃƒÂ  multiplier n'est pas de la classe BooleanMatrix")
                
                
                if len(self.coefficients) != len(matrice.coefficients[0]):
                        raise TypeError("Les deux matrices ne sont pas de dimensions pouvant ÃƒÂªtre multipliÃƒÂ©es")
                
                coeffs = []
                for i in range (len(self.coefficients)) :#pour chaque dimension
                        ligne = []
                        for j in range(len(matrice.coefficients[0])) :      #pour chaque dimension
                                coeff = 0
                                for k in range (len(self.coefficients[0])) :    #pour chaque dimension
                                       
                                        coeff += self.coefficients[i][k] * matrice.coefficients[k][j]#On calcule le produit des coefficients
                                        if coeff > 1 :
                                                coeff = 1
                                        
                                ligne.append(coeff)#Les matrices sont Ã©crites de cette facon : [[ligne],[ligne],[ligne]]
                        coeffs.append(ligne)
                                
                M = BooleanMatrix(coeffs)
                return M

        def add(self, matrice):
                if type(matrice) != type(self):
                        raise TypeError("La matrice ÃƒÂ  ajouter n'est "
                            + "pas de la classe BooleanMatrix")

                longueur = len(self.coefficients)
        
                if len(matrice.coefficients) != longueur:
                        raise TypeError("La matrice ÃƒÂ  ajouter n'est pas de la mÃƒÂªme taille")
          
                for i in range(longueur):
                            for j in range(longueur):
                                self.coefficients[i][j] = min(1, self.coefficients[i][j] + matrice.coefficients[i][j])

        def copy(self, var_out):
            """
            this function copy the booleanmatrix object into var_out
            """
            var_out.coefficients = self.coefficients

                         
if __name__ == '__main__':
        Z = BooleanMatrix([[0,0],[0,0]])
        A = BooleanMatrix([[1,1,0,1,0],[1,1,1,1,1],[0,0,1,1,0],[1,1,0,0,0],[1,0,0,1,0]])
        B = BooleanMatrix([[1,1,0,1,0],[0,0,0,0,0],[0,1,1,1,0],[1,1,0,0,0],[1,0,0,1,0]])
        C = BooleanMatrix([[1,1],[1,1]])
        D = BooleanMatrix([[1,0],[0,1]])
        E = BooleanMatrix([[1,0],[0,1]])
        F = BooleanMatrix([[1,0],[1,1]])
        G = BooleanMatrix([[0,0],[0,1]])
        H = BooleanMatrix([[1,1],[0,0]])
         
