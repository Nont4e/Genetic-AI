import numpy
import random
import math

answer = "print(42)"
population = []
pool = []
max_fitness = 0

def Create_Population(N):
    for x in range(int(N)):
        gene = ""
        while len(gene) < 9:
            #Pool of population is ASCII Code 32-126 (All character, number, symbol)
            chrm = random.randint(32,126)
            gene += (chr(chrm))
        population.append(gene)
        fitness = Cal_Fitness(gene)
        population.append(fitness)

def Cal_Fitness(gene):
    score = 0
    for x in range(9):
        if(gene[x] == answer[x]):
            score = score + 1
    if(max_fitness < score):
        max_fitness = score
    return score

def Create_RandomPool(population):
    for gene in population:
        #Get a fitness
        fitness = math.floor(gene[len(gene) - 1] * 100)
        #Insert gene in the pool. More fitness, more prob to be selected.
        for x in range(fitness):
            pool.append(gene)

def Generate_child():
    p1 = random.choice(pool)
    p2 = random.choice(pool)
    while p1 == p2:
        p2 = random.choice(pool)
    
    

            
create_population(100)