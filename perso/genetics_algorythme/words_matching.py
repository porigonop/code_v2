import random
import time
def profile(func):
    return func

# RANDOM_OBJECT = random.Random(0)
RANDOM_OBJECT = random
DEBUG = False
POSSIBLE_VALUES = " abcdefghijklmnopqrstuvwxyz0123456789"
class Individual:
    current = []
    value_pool = []
    length = 0
    length_value_pool = 0
    def __init__(self, length=0, value_pool=POSSIBLE_VALUES, forced_value=None):
        self.value_pool = value_pool
        self.length_value_pool = len(self.value_pool)
        if forced_value is not None:
            self.current = forced_value
        else:
            if length < 0:
                raise Exception('length must be set if no forced value')
            self.current = [self.value_pool[int(RANDOM_OBJECT.random() * self.length_value_pool)] for _ in range(length)]
        self.length = len(self.current)


    def mutate(self, mutation_rate):
        # FIXME : do a more random choice of number of index to change
        # goal : for index in indexes: if random() > mutation_rate: number.append(index)
        number_of_index_to_change = int(mutation_rate * self.length)
        indexes_to_change = [int(RANDOM_OBJECT.random() * self.length) for _ in range(number_of_index_to_change)]
        for index in indexes_to_change:
            self.current[index] = self.value_pool[int(RANDOM_OBJECT.random() * self.length_value_pool)]

    def breed(self, other):
        new_values = []
        len_new_values = 0
        while len_new_values < self.length:
            size_to_select = 1 + int(RANDOM_OBJECT.random() * (self.length - len_new_values))
            if RANDOM_OBJECT.random() < 0.5:
                new_values += self.current[len_new_values:len_new_values + size_to_select]
            else:
                new_values += other.current[len_new_values:len_new_values + size_to_select]
            len_new_values += size_to_select
        return Individual(len_new_values, value_pool=self.value_pool, forced_value=new_values)

    def get_fitness(self, fitness_function):
        return fitness_function(self.current)

    def __str__(self):
        return "".join([str(value) for value in self.current])

    def __repr__(self):
        return str(self)




class Population:
    population = []
    def __init__(self, population_size=-1, length_individual=-1, value_pool=POSSIBLE_VALUES, forced_population=None):
        if forced_population is not None:
            self.population = forced_population
        else:
            if population_size < 0:
                raise Exception('population_size must be set if no forced population')
            if length_individual < 0:
                raise Exception('length_individual  must be set if no forced population')
            self.population = [Individual(length_individual, value_pool=value_pool)\
                    for _ in range(population_size)]

    def get_fitness_for_individual(self, fitness_function):
        return [(individual.get_fitness(fitness_function), individual)
                for individual in self.population]
    def get_average_fitness(self, fitness_function):
        return sum(map(lambda value: value[0],
            self.get_fitness_for_individual(fitness_function)))\
                    / len(self.population)

    def get_fitness_percent(self, fitness_function, max_fitness):
        return (self.get_average_fitness(fitness_function) / max_fitness) * 100

    def get_max_fitness_percent(self, fitness_function, max_fitness):
        return (max(map(lambda x: x[0], self.get_fitness_for_individual(fitness_function))) / max_fitness) * 100

    def get_best_individual(self, fitness_function):
        return self.sort_population_by_best_fitness(fitness_function)[0][1]

    def sort_population_by_best_fitness(self, fitness_function):
        fitness_values = self.get_fitness_for_individual(fitness_function)
        return sorted(fitness_values, key=lambda value: value[0], reverse=True)

    @profile
    def choose_individual(self, sorted_pop, choice, min=0, max=None):
        """
        sorted_pop : the population sorted, a tuple with an aggregated fitness
                     [(2, 'aa'), (4, 'aa'), (5, 'ab'), (6, 'ab'), (6, 'bb')]
                     for exemple, every fitness value is the sum of the
                     previous one, plus the fitness of the current one
                     with fit('aa') == 2, fit('ab') == 1, fit('bb') == 0
        choice : the number choosen : for the sorted_pop above, if choice == 2:
                 the 1st individual must be returned, if choice is 5, the 3rd one
        min/max : not argument, usefull for recursive purpuse
        this function perform a 'binary search' more or less
        """
        if max == min or max == min + 1:
            return sorted_pop[min][1]
        if max is None:
            max = len(sorted_pop)
        mid_point = min + ((max - min) // 2)
        if sorted_pop[mid_point][0] > choice:
            return self.choose_individual(sorted_pop, choice, min=min, max=mid_point)
        return self.choose_individual(sorted_pop, choice, min=mid_point, max=max)

    def aggregate_sum(self, sorted_pop):
        current_sum = 0
        new_pop = []
        for fitness, individual in sorted_pop:
            current_sum += fitness
            new_pop.append((current_sum, individual))
        return new_pop

    def evolve_to_next_generation(self, fitness_function, population_size=None, mutation_rate=0.1):
        if population_size is None:
            population_size = len(self.population)
        sorted_pop = self.sort_population_by_best_fitness(fitness_function)
        sorted_pop = self.aggregate_sum(sorted_pop)
        sum_fitness = sorted_pop[-1][0]
        new_population = []
        for _ in range(population_size):
            if RANDOM_OBJECT.random() < mutation_rate:
                new_population.append(Individual(self.population[0].length, value_pool=self.population[0].value_pool))
                continue
            choice1 = RANDOM_OBJECT.random() * sum_fitness
            choice2 = RANDOM_OBJECT.random() * sum_fitness
            individual1 = self.choose_individual(sorted_pop, choice1)
            individual2 = self.choose_individual(sorted_pop, choice2)
            new_individual = individual1.breed(individual2)
            new_individual.mutate(mutation_rate)
            new_population.append(new_individual)
        return Population(forced_population=new_population)

    def __str__(self):
        return self.str_number(len(self.population))
    def str_number(self, number):
        return "[\n" + ",\n".join([str(individual) for individual in self.population[:number]]) + "\n]"



def create_fitness_function(string_to_match):
    def fitness_function(current):
        res = 0
        for current_char, string_char in zip(current, string_to_match):
            if (current_char == string_char):
                res += 1
        return res
    return fitness_function

def create_another_fitness_function(length):
    string_to_match = [RANDOM_OBJECT.choice(POSSIBLE_VALUES) for _ in range(length)]
    def fitness_function(current):
        res = 0
        for current_char, string_char in zip(current, string_to_match):
            if (current_char == string_char):
                res += 1
        return res
    return fitness_function

def create_cible_fitness_function(coordonne, max_distance_sq):
    def fitness_function(current):
        coord_initial = [0, 0]
        i = 1
        for x, y in current:
            coord_initial[0] += x
            coord_initial[1] += y
            if coordonne[0] == coord_initial[0] and coordonne[1] == coord_initial[1]:
                return max_distance_sq - i
            i += 1
        distance_sq = (coord_initial[0] - coordonne[0])**2 + (coord_initial[1] - coordonne[1]) ** 2
        return (max_distance_sq - distance_sq) - i
    return fitness_function

def test_rocket():
    possible_values = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
    population = Population(100, 10, value_pool=possible_values)
    fitness_function = create_cible_fitness_function((10, 10), 10000** 2)
    i = 0
    for i in range(500):
        population = population.evolve_to_next_generation(fitness_function, mutation_rate=0.01)
        best_ind = population.get_best_individual(fitness_function)
    print(i)
    best_ind = population.get_best_individual(fitness_function)
    DEBUG = True
    print(best_ind.get_fitness(fitness_function))


if __name__ == "__main__":
    start = time.time()
    value_to_match = 'factorio est le meilleur jeu de toute la planete'
    # pop = Population(50, len(value_to_match), value_pool='agtc')
    pop = Population((len(value_to_match)**2 + 200) * 2, len(value_to_match), value_pool=POSSIBLE_VALUES)
    fitness_function = create_fitness_function(value_to_match)
    # fitness_function = create_another_fitness_function(len(value_to_match))
    # print(pop)
    print(len(pop.population))
    for i in range(10000):
        pop = pop.evolve_to_next_generation(fitness_function, mutation_rate=0.01)
        best_individual = pop.get_best_individual(fitness_function)
        print(best_individual)
        if best_individual.get_fitness(fitness_function) == len(value_to_match):
            print("found :", best_individual)
            break
        # time.sleep(0.1)
        if i % 100 == 0:
            print(pop.get_fitness_percent(fitness_function, len(value_to_match)),
                    pop.get_max_fitness_percent(fitness_function, len(value_to_match)))
    # DEBUG = True

    pop = pop.evolve_to_next_generation(fitness_function, mutation_rate=0.1)
    print(pop.get_fitness_percent(fitness_function, len(value_to_match)))
    stop = time.time()
    print('time: ', stop - start)


