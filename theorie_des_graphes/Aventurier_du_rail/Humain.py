from Joueur import Joueur
from CarteWagon import CarteWagon

class Humain(Joueur):
    """
    défini le joueur humain
    """
    def jouer(self, plateau):
        """
        permet a un humain de jouer
        """
        print("le joueur " + self.color + " joue")

        print("il possédes les cartes wagons suivantes : ")

        for carte in self.carte_wagon:
            print(carte)
        print("il possédes les cartes destination : ")
        for carte in self.carte_destination:
            print(carte)
            print("--------")
        print("et il lui reste : " +\
         str(len(self.reserve_de_wagon)) \
         + " wagons")
        print("enfin le plateau est : ")
        print("--------------------------")
        print(plateau.graph)
        print("que voulez vous faire ?\n"+\
              "1 : prendre carte wagon\n" + \
              "2 : prendre carte destination"+\
              "3 : poser une route")
        while True:
            answer = input()
            if answer == "1":
                self.prendre_wagon(plateau)
                return True
            elif answer == "2":
                self.prendre_destination(plateau)
                return True

            elif answer == "3":
                if self.poser_route(plateau):
                    return True
                else:
                    print("erreur, que voulez vous faire :")
                    print("1 : prendre carte wagon\n" + \
                          "2 : prendre carte destination"+\
                          "3 : poser une route")
                    continue

    def prendre_wagon(self, plateau):
        """
        permet de prendre un wagon
        """
        print("les wagons visibles sont : ")
        for index in len(plateau.visible):
            print(index, " : ", plateau.visible[index])

        while True:
            print("indiquer le numero si vous voulez prendre une carte visible"+\
            " sinon pressez entrer")
            answer = input()
            if answer == "":
                carte = plateau.pioche_wagon.pick()
                self.carte_wagon.append(carte)
                print("vous piocher une " + str(carte))
                break
            else:
                try:
                    answer = int(answer)
                except ValueError:
                    print("vous n'avez pas entré un chiffre")
                    continue
                if answer in range(5):

                    carte = plateau.visible.pop(answer)
                    self.carte_wagon.append(carte)
                    plateau.visible.append(plateau.pioche_wagon.pick())
                    print("vous piocher une " + str(carte))
                    if carte.color == "multicolor":
                        return
                    break
            print("couleur non trouvée")

        print("les wagon visibles sont : ")
        for carte in plateau.visible:
            print(carte)

        while True:
            print("indiquer une couleur si vous voulez prendre une carte"\
            +" visible sinon pressez entrer")
            answer = input()
            if answer == "":
                carte = plateau.pioche_wagon.pick()
                self.carte_wagon.append(carte)

                print("vous piocher une " + str(carte))
                break
            else:
                try:
                    answer = int(answer)
                except ValueError:
                    pass
                if answer in range(5):
                    carte = plateau.visible.pop(answer)
                    if carte.color == "multicolor":
                        plateau.visible.append(carte)
                        continue
                    self.carte_wagon.append(carte)
                    plateau.visible.append(plateau.pioche_wagon.pick())
                    print("vous piocher une " + str(carte))
                    break
            print("couleur non trouvée")

    def prendre_destination(self, plateau):
        """
        permet de piocher une carte destination sur le plateau
        """
        lst = []
        for i in range(3):
            try:
                lst.append(plateau.pioche_destination.pick())
            except IndexError:
                print("il n'y avait pas assez de cartes")
                break
        print("voici vos cartes destination")
        for carte in lst:
            print(carte)
            print("----------------")
        impo = True
        while impo:
            print("choississez les cartes voulu en indiquant leur positions, séparé d'un éspace")
            answer = input()
            answer = sorted(answer.split(" "))
            answer.reverse()
            impo = False
            for elt in answer:
                if int(elt) >= len(lst):
                    print("impo")
                    impo = True
            if impo:
                continue

            for i in answer:
                i = int(i)
                self.carte_destination.append(lst.pop(i))
            for carte in lst:
                plateau.pioche_destination.pioche.append(carte)

    def poser_route(self, plateau):
        """
        permet de choisire une route et de jouer dessus si possible
        """
        while True:
            depart = input("ville de départ (pour annuler, entrer annuler): ")
            if depart == "annuler":
                return False
            if not depart in plateau.graph.nodes:
                print("mauvais nom de ville")
                continue

            arriver = input("ville d'arriver : ")

            if depart == arriver or not arriver in plateau.graph.nodes:
                print("mauvais nom de ville, retour à la ville de depart")
                continue

            if not depart in plateau.graph.adjacency_list[arriver] \
            or (depart, arriver) in plateau.used:
                print("la route n'est pas disponible")
                continue
            print((depart, arriver), plateau.used)
            for edge in plateau.graph.edges:
                if edge[0] == depart and edge[1] == arriver:
                    if len(self.reserve_de_wagon) < edge[2]:
                        print("pas assez de wagons")
                    else:
                        if edge[3] != "Gris":
                            cartes = [carte for carte in self.carte_wagon if carte.color == edge[3]]
                        else:
                            for i in range(edge[2]):
                                cartes = []
                                while True:
                                    print("quelle couleur utiliser ?")
                                    couleur = input()
                                    if couleur in [carte.color for carte in self.carte_wagon]:
                                        for carte in self.carte_wagon:
                                            if carte.color == couleur:
                                                cartes.append(carte)
                                                break
                                        break

                        if len(cartes) < edge[2]:
                            print("pas assez de carte :", len(cartes), "<", edge[2])
                            if not edge[2] > len([carte.color for carte in self.carte_wagon if carte.color == "multicolor"] + carte):
                                print("voulez vous ajouter des cartes multicolor ?")
                                answer = input()
                                if answer == "oui":
                                    for i in range(edge[2] - len(carte)):
                                        for carte in self.carte_wagon:
                                            if carte.color == "multicolor":
                                                cartes.append(carte)
                        if len(cartes) == edge[2]:
                            print("Vous avez pris posséssion de la route !")
                            plateau.used.append((depart, arriver))
                            plateau.used.append((arriver, depart))
                            plateau.uscol.append(self.color)
                            plateau.value_uscol.append(edge[2])
                            plateau.edgecolor[str(edge)] = self.color
                            while len(cartes) != 0:
                                self.carte_wagon.remove(cartes.pop())

                            return True
