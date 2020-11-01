from random import randint
from math import sqrt
from math import ceil
from random import random

#Each suggested solution for a genetic algorithm is referred to as an individual
def individual(length,max):
    #create a member of the population
    singleList = []
    singleList = [randint(0,ceil(sqrt(max))) for x in range(length)]
    return singleList

#The collection of all indiciduals is referred to as our population
def population(count,length,max):
    '''
    create a number of individuals.
    count: the number of indiciduals in the population
    Length: the number of values per individual
    max: the max possible value in an individual's list of values
    '''
    pop = []
    pop = [individual(length,max)for x in range(count)]
    return pop

#Next, we need a way to judge the how effective each solution is;to judge the fitness of each individual. Predictably enough, we call this the fitness function
def fitness(individual, target):
    '''
    Determine the fitness of an indicidual.
    individual: the individual to evaluate
    target: the sum of numbers that individuals are aiming for
    '''
    sum = 0
    for x in individual:
        sum = sum + x *x
    return abs(target - sum)
# This just like taking individuals who are not performing particularly well-is to encourage genetic diversity, i.e.avoid getting stuck at local maxima
def evolve(pop,target,retain = 0.2,random_select = 0.05,mutate = 0.01):
    graded = []
    graded = [(fitness(x,target),x)for x in pop]
    popula = list(pop)
    parent=[]
    retain_length = round(len(pop) * retain)

    while retain_length>0:
        num = 0
        test =0
        for x in graded:
            if x <graded[0]:
                graded[0] = x
                test = num
            num =num +1
        
        parent.append(popula[test])
        popula.pop(test)
        graded.pop(test)
        retain_length = retain_length-1
# randomly add other individuals to promote genetic diversity
    for singleList in popula:
        if random_select > random():
            parent.append(singleList)

# mutate some individuals
    for individual in parent:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(0, ceil(sqrt(target)))
                
# crossover parents to create children
    parents_length = len(parent)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parent[male]
            female = parent[female]
            half = randint(0,len(male))
            child = male[:half] + female[half:]
            children.append(child)        
    children.extend(parent)
    return children

#find the best result
def result(length, target, retain=0.2, random_select=0.05, mutate=0.01):
   
    
    populationList = population(100,length,target)
    
    boolen = False
    n = 0

    while not boolen:
        populationList = (evolve(populationList,target, retain, random_select, mutate))
        
        for x in populationList:
            if (fitness(x, target) == 0):
                print(x)
                boolen = True
                break
        if boolen is True:
            break

        if n % 15 == 0:
            if random_select < 0.8:
                random_select = random_select + 0.015
            if retain < 0.8:
                retain =retain + 0.015
            if mutate < 0.8:
                mutate =mutate + 0.015
                
        n = n+1
    return

#Test
def main():

    print("Creating a list of 6 numbers that equal 500 when squared and summed together: ")
    result(6, 500)
    return

main()