import numpy
import random
import math

answer = "print(42)"
population = []
pool = []
max_fitness = 0
mutationRate = 0.0
bestPhrase = ""
avg_fitness = 0

def Create_Population(N):
    global population
    global avg_fitness
    for x in range(int(N)):
        #In cell contain 2 variable: gene and fitness e.g.['print(42)', 100]
        cell = []
        gene = ""
        while len(gene) < 9:
            gene += Create_NewGene()
        cell.append(gene)
        #Find fitness of each gene
        fitness = Cal_Fitness(gene)
        cell.append(fitness)
        population.append(cell)
    avg_fitness = avg_fitness / len(population)
    print("Generation: 0\nBest Phrase: " + bestPhrase + "\nMax_Fitness: " + str(max_fitness) + "%\nAvg_Fitness: " + str(avg_fitness) + "%\n")
         
def Create_NewGene():
    #Pool of population is [()][0-9][a-z]
    num = random.randint(0,37)
    #Bracket
    if(num <= 1): 
        num += 40
    #Digit
    elif(num <= 11): 
        num += 46
    #Alphabet
    else:
        num += 85
    return chr(num)

def Cal_Fitness(gene):
    global avg_fitness
    global max_fitness
    global bestPhrase
    score = 0
    for x in range(9):
        if(gene[x] == answer[x]):
            score += 1
    #Change to percentage
    score = score / 9 * 100
    #Find the best one
    avg_fitness += score
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
    global pool
    global bestPhrase
    global max_fitness
    global avg_fitness
    max_fitness = 0
    bestPhrase = ""
    for x in range(len(population)):
        #Create new child
        p1 = random.choice(pool)
        p2 = random.choice(pool)
        child = Mutation(Crossover(p1,p2), Mrate)
        #Replace the old gen with the new gen 
        population[x][0] = child
        population[x][1] = Cal_Fitness(child)
    avg_fitness = avg_fitness / len(population)
    #Print best result of each generation
    print('Generation: '+ str(gen) + "\nBest Phrase: " + bestPhrase + "\nFitness: " + str(max_fitness) + "%\nAvg_Fitness: " + str(avg_fitness) + "%\n")

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
    MutatedChild = ""
    for a in child:
        mutated = random.randint(0,100) / 100
        #If the prob. of Mutated of each alphabet is less than or equal Mutated rate, mutate it
        if(mutated <= Mrate):
            mutatedA = Create_NewGene()
            #If the new one is same as the old one
            while mutatedA == a:
                mutatedA = Create_NewGene()
            a = mutatedA
        MutatedChild += a     
    return MutatedChild
        
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
Genetic(100,0.5)
