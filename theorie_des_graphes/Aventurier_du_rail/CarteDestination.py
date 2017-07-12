#usr/bin/env python3
####################
#
#
#
#
####################
class CarteDestination:
    """ """

    def __init__(self, departure, arrival, value):
        """ """
        self.departure = departure
        self.arrival = arrival
        self.value = value


    def __repr__(self):
        """ """
        return 'Point de départ ---> ' + self.departure + ' \n'\
                + ' Point d''arrivée ---> ' + self.arrival + '\n'\
                + 'valeur : ' + str(self.value)
    
               
