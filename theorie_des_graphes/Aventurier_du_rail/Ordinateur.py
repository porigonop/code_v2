#usr/bin/env python3
from random import random
from Joueur import Joueur
class Ordinateur(Joueur):
    """ Class which inherits from class Joueur. It allows to play against
        a computer """
    def jouer(self, plateau):
        """ """
        a_jouer = False
        cartes = []
        for edge in plateau.graph.edges:
            if len(self.reserve_de_wagon) >= edge[2]:
                if len(self.carte_wagon) >= edge[2] and edge[3] == "Gris":
                    if not (edge[0], edge[1]) in plateau.used:
                        for carte in self.carte_wagon:
                            if carte.color == edge[3]:
                                cartes.append(carte)

                        plateau.used.append((edge[0], edge[1]))
                        plateau.used.append((edge[1], edge[1]))
                        plateau.uscol.append(self.color)
                        plateau.values_uscol.append(edge[2])
                        plateau.edgecolor[str(edge)] = self.color
                        a_jouer = True
                        while len(cartes) != 0:
                            carte = cartes.pop()
                            self.reserve_de_wagon.pop()
                            self.carte_wagon.remove(carte)
                            plateau.pioche_wagon.defausse(carte)
                        break
                if len([carte for carte in self.carte_wagon if carte.color == edge[3]]) >= edge[2]:
                    if not (edge[0], edge[1]) in plateau.used:
                        for carte in self.carte_wagon:
                            if carte.color == edge[3]:
                                cartes.append(carte)

                        plateau.used.append((edge[0], edge[1]))
                        plateau.used.append((edge[1], edge[1]))
                        plateau.uscol.append(self.color)
                        plateau.values_uscol.append(edge[2])
                        plateau.edgecolor[str(edge)] = self.color
                        a_jouer = True
                        print(self.color, "as pris la route :", edge[0], edge[1], "de couleur :", edge[3])
                        while len(cartes) != 0:
                            carte = cartes.pop()
                            self.reserve_de_wagon.pop()
                            self.carte_wagon.remove(carte)
                            plateau.pioche_wagon.defausse(carte)
                        break
        if not a_jouer:
            try:
                self.carte_wagon.append(plateau.pioche_wagon.pick())
                self.carte_wagon.append(plateau.pioche_wagon.pick())
                print(self.color, "as piocher une carte wagon")
            except:
                print(self.color, "plus de carte dans la pioche, mon faible esprit ne me permet pas de continuer la partie, je déclare forfait")
                return False
        


