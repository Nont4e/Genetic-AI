import numpy
import random
import math

answer = "print(42)"
population = []
pool = []
max_fitness = 0
mutationRate = 0.0
bestPhrase = ""

def Create_Population(N):
    population = []
    for x in range(int(N)):
        cell = []
        gene = ""
        while len(gene) < 9:
            #Pool of population is ASCII Code 32-126 (All character, number, symbol)
            num = random.randint(32,126)
            gene += (chr(num))
        cell.append(gene)
        fitness = Cal_Fitness(gene)
        cell.append(fitness)
        population.append(cell)
    return population, 

def Cal_Fitness(gene):
    global max_fitness
    global bestPhrase
    score = 0
    for x in range(9):
        if(gene[x] == answer[x]):
            score = score + 1
    if(max_fitness < score):
        max_fitness = int(score / 9 * 100)
        bestPhrase = gene
    return score

def Create_RandomPool():
    pool = []
    for cell in population:
        #Get a fitness
        fitness = math.floor(cell[1] * 100)
        #Insert gene in the pool. More fitness, more prob to be selected.
        for x in range(fitness):
            pool.append(cell)
    return pool

def Create_NewGeneration(gen, Mrate):
    for x in range(len(population)):
        p1 = random.choice(pool)
        p2 = random.choice(pool)
        child = Mutation(Crossover(p1,p2), Mrate)
        population[x] = child
    #Print result of each generation
    print('Generation: '+ str(gen) + "\nBest Phrase: " + bestPhrase + "\nFitness: " + str(max_fitness) + "\n")

def Crossover(p1, p2):
    child = ""
    pivot = random.randint(0,9)
    for x in range(9):
        if(x < pivot):
            child += p1[x]
        else:
            child += p2[x]
    return child

def Mutation(child, Mrate):
    for a in child:
        mutated = random.randint(0,9) / 100
        if(mutated >= Mrate):
            mutatedA = chr(random.randint(32,126))
            while mutatedA == a:
                mutatedA = chr(random.randint(32,126))
            a = mutatedA
    return child
        
def Genetic(NumofPop, Mrate):
    generation = 1
    Create_Population(NumofPop)
    Create_RandomPool()
    while(max_fitness != 100):
       Create_NewGeneration(generation, Mrate)
       generation = generation + 1

#Run Code
Genetic(1000,0.1)