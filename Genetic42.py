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
    global population
    for x in range(int(N)):
        #In cell contain 2 variable: gene and fitness e.g.['print(42)', 100]
        cell = []
        gene = ""
        while len(gene) < 9:
            #Pool of population is ASCII Code 32-126 (All character, number, symbol)
            num = random.randint(32,126)
            gene += (chr(num))
        cell.append(gene)
        #Find fitness of each gene
        fitness = Cal_Fitness(gene)
        cell.append(fitness)
        population.append(cell) 

def Cal_Fitness(gene):
    global max_fitness
    global bestPhrase
    score = 0
    for x in range(9):
        if(gene[x] == answer[x]):
            score = score + 1
    #Change to percentage
    score = score / 9 * 100
    #Find the best one
    if(max_fitness < score):
        max_fitness = score
        bestPhrase = gene
    return score

def Create_RandomPool():
    global pool
    global population
    pool.clear()
    for cell in population:
        #Get a fitness
        fitness = math.floor(cell[1] * 100)
        #Insert gene in the pool. More fitness, more prob to be selected.
        for x in range(fitness):
            pool.append(cell)

def Create_NewGeneration(gen, Mrate):
    for x in range(len(population)):
        #Create new child
        p1 = random.choice(pool)
        p2 = random.choice(pool)
        child = Mutation(Crossover(p1,p2), Mrate)
        #Replace the old gen with the new gen 
        population[x][0] = child
        population[x][1] = Cal_Fitness(child)
    #Print best result of each generation
    print('Generation: '+ str(gen) + "\nBest Phrase: " + bestPhrase + "\nFitness: " + str(max_fitness) + "%\n")

def Crossover(p1, p2):
    child = ""
    pivot = random.randint(0,9)
    for x in range(9):
        if(x < pivot):
            child += p1[0][x]
        else:
            child += p2[0][x]
    return child

def Mutation(child, Mrate):
    for a in child:
        mutated = random.randint(0,9) / 100
        #If the prob. of Mutated of each alphabet is more than or equal Mutated rate, mutate it
        if(mutated >= Mrate):
            mutatedA = chr(random.randint(32,126))
            #If the new one is same as the old one
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
       Create_RandomPool()

#Run Code
#Genetic(NumberofPopulation, MutationRate)
Genetic(1000,0.1)
