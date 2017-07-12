#!/usr/bin/env python3
import random
import numpy as np
from pprint import pprint

class Neurone:
    """
    describe the neurone object
    """
    def __init__(self, nb_of_entry, weights = [], sill = 0):
        """
        create a neurone
        if weights is not define, create a random
        neurone with number_of_entry entry
        else create a neurone with a list of weight
        and sill as sill
        """
        if weights == []:
            self.weights = [round(random.random(), 2) \
                for i in range(nb_of_entry)]
            self.sill = round(random.random(), 2)
            
        else:
            self.weights = weights
            self.sill = sill
    
    def multiply(self, entry):
        """
        define the multiplicate between our weights
        and each item in the list entry
        """
        result = []
        if len(entry) != len(self.weights):
            raise ValueError("error incorect len of liste")
        for pos in range(len(entry)):
            result.append(entry[pos] * \
                self.weights[pos])
        return result
    
    def run(self, entry):
        """
        run the neurone with the list entry as entry
        return 1 if neurone activate
        0 if not
        """
        
        if sum(self.multiply(entry)) > self.sill:
            return 1
        else:
            return 0

    def __repr__(self):
        """
        a representation that allows us to 
        recreate the neurone
        """
        string = "Neurone(1, ["
        for weight in self.weights:
            string = string + str(weight) + ", "
        string = string[:-2]+ "]"
        string = string + ", "  + str(self.sill)
        return string + ")"

class NeuralNetwork:
    """
    describe the neuralnetwork
    """
    def __init__(self, inpt = [], hidden = [], output = []):
        """
        inpt is not define
        allow the user to create a random 
        neuralnetwork if 
        
        else
        it will create a neuralnetwork with 
            -> a list inpt of input neurone
            -> a list hidden of hidden neurone
            -> a list output of output neurone
        """
        if inpt == []:
            self.input = [Neurone(1) \
                for i in range(2)]
            self.hidden = [Neurone(2) \
                for i in range(3)]
            self.output = [Neurone(3) \
                for i in range(1)]
        else:
            self.input = inpt
            self.hidden = hidden
            self.output = output
    def run(self, entry):
        """
        run the neuralnetwork with the list entry
        of input
        notice that each input is a list :
        [[1], [1]] to input 1 and 1
        """
        if len(entry) != len(self.input):
            raise ValueError("incorrect len")
        tmp = []
        """
        for neurone in self.input:
            if neurone.run(entry) == 1:
                tmp.append(1)
            else:
                tmp.append(0)
        """
        for pos in range(len(self.input)):
            if self.input[pos].run(entry[pos])\
                    == 1:
                tmp.append(1)
            else:
                tmp.append(0)
        #"""
        tmp1 = []
        for neurone in self.hidden:
            if neurone.run(tmp) == 1:
                tmp1.append(1)
            else:
                tmp1.append(0)
                
        result = []
        for neurone in self.output:
            if neurone.run(tmp1) == 1:
                result.append(1)
            else:
                result.append(0)
        return result
        
    def croisement(self, neuralnetwork):
        """
        allows the croisement between 2 neuralnetworks
        """
        pass
        
        
        
    def __repr__(self):
        """
        a representation that alows us to recreate the neuralnetwork
        """
        string = "NeuralNetwork(\n[\n"
        for neurone in self.input:
            string = string + str(neurone) + ", \n"
        string = string[:-3] + "], \n[\n"
        for neurone in self.hidden:
            string = string + str(neurone) + ", \n"
        string = string[:-3] + "], \n[\n"
        for neurone in self.output:
            string = string + str(neurone) + ", \n"
        
        return string[:-3] + "])"

class Population:
    """
    describe a populaion of neuralnetwork
    """
    def __init__(self, number_in_population = 5):
        """
        create a list of nb neuralnetwork
        """
        self.population = [NeuralNetwork() for i in range(number_in_population)]
        
    def run(self, entry, answer):
        """
        run the entire list of neuralnetwork and return a list with the success or echec of each neuralnetwork like :
        [0, 1, 1, 0, 1]
        
        """
        result = []
        for neuralnetwork in self.population:
            tmp = neuralnetwork.run(entry)
            if tmp == [answer]:
                result.append(1)
            else:
                result.append(0)
        return result
        
    def find_most_valuable_neuralnetwork(self):
        """
        run all the test and return all the best result of
        neuralnetwork in a list 
        
        NOTFINISHED
        """
        
        test1 = np.array(self.run([ [1], [1] ], 1))
        test2 = np.array(self.run([ [1], [0] ], 0))
        test3 = np.array(self.run([ [0], [1] ], 0))
        test4 = np.array(self.run([ [0], [0] ], 0))
        
        """
        a = np.array(self.run([1, 1], 1))
        b = np.array(self.run([1, 0], 0))
        c = np.array(self.run([0, 1], 0))
        d = np.array(self.run([0, 0], 0))
        """
        global_success = test1 + test2 + test3 + test4
        
        higher_value = 4 #max(global_success)
        print (higher_value)
        best_of_population = []
        for pos in range(len(self.population)):
            if global_success[pos] \
                    == higher_value:
                best_of_population.append\
                    (self.population[pos])
        return(best_of_population)
        #new_pop = meilleur + [NeuralNetwork() \
        #    for i in range(len(self.population) - len(meilleur))]
        
        self.population = new_pop
if __name__ == "__main__":
    A = Population()
    #if a neural network satisfy the thing, return it
    print(A.find_most_valuable_neuralnetwork())
    
    #his neural network satisfy
    answer = NeuralNetwork(
[
Neurone(1, [0.94], 0.46), 
Neurone(1, [0.77], 0.69)], 
[
Neurone(1, [0.72, 0.63], 0.43), 
Neurone(1, [0.29, 0.43], 0.57), 
Neurone(1, [0.69, 0.59], 0.17)], 
[
Neurone(1, [0.17, 0.15, 0.12], 0.3)])
    print("1 and 1", answer.run([[1], [1]]))
    print("1 and 0", answer.run([[1], [0]]))
    print("0 and 1", answer.run([[0], [1]]))
    print("0 and 0", answer.run([[0], [0]]))
