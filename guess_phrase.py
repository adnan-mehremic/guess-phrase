import random

population_size = 150
target = "Machine learning is awesome."
genes = '''qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890 ,.-_;:?!@$'''
# percente value of elitism to be performed
elitism_factor = 10
mating_percent = 50


class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness_score = self.calculate_fitness()

    @classmethod
    def mutated_genes(self):
        # create a competely random chromosome
        global genes
        rand_gene = random.choice(genes)
        return rand_gene

    @classmethod
    def create_gnome(self):
        # create a new choromosome
        global target
        gnome_length = len(target)
        return [self.mutated_genes() for _ in range(gnome_length)]

    def mate(self, second_parent):
        # create a new offspring (using 2 parents)
        child_chromosome = []

        for gp1, gp2 in zip(self.chromosome, second_parent.chromosome):
            probability = random.random()
            if probability < 0.45:
                child_chromosome.append(gp1)

            elif probability < 0.90:
                child_chromosome.append(gp2)

            else:

                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)


    def calculate_fitness(self):
        global target
        fitness_score = 0
        # cg - character from generation
        # ct - character from text
        for cg, ct in zip(self.chromosome, target):
            if cg != ct:
                fitness_score += 1
        return fitness_score


def main():
    global population_size
    global elitism_factor
    global mating_percent
    population = []
    is_solved = False
    generation_number = 1

    # create the initial population
    for _ in range(population_size):
        # generate a new chromosome
        gnome = Individual.create_gnome()
        # generate a new individual
        new_individual = Individual(gnome)
        population.append(new_individual)

    while not is_solved:
        population = sorted(population, key=lambda x: x.fitness_score)
        # if we have solved the problem break out of the loop
        if population[0].fitness_score <0:
            is_solved = True
            break

        new_population = []

        # elitism
        s = int((elitism_factor*population_size)/100)
        new_population.extend(population[:s])

        # perform the process of mating
        mating_factor = 100 - elitism_factor
        s = int((mating_factor * population_size) / 100)

        for _ in range(s):
            real_population = int((mating_percent*population_size)/100)

            parent_1 = random.choice(population[:real_population])
            parent_2 = random.choice(population[:real_population])
            child = parent_1.mate(parent_2)
            new_population.append(child)

        population = new_population

        print("Generation: {}\tString: {}\t Fitness: {}". \
              format(generation_number,
                     "".join(population[0].chromosome),
                     population[0].fitness_score))

        generation_number += 1


if __name__ == '__main__':
    main()
