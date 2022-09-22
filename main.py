from random import random, randint
from math import ceil, floor
import string


optiml_solution = 'Farah1 Areen2 Mutasem2 Hasan4 Hesham5 Bara6'

char_fit = 100 / len(optiml_solution)
mutation_percentage = 0
iterations = 3000
pop_num = 300
_highest_score = 0
_highest_score_record = ''
full_EN_char_list = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [" "] + [str(x) for x in list(range(0,10))]
init_pop = []
solution = []

for i in range(0, pop_num):
    rand_record = []
    for i in range(0, len(optiml_solution)):
        rand_record.append(full_EN_char_list[randint(0, len(full_EN_char_list) - 1)])
    init_pop.append("".join(rand_record))

solution = []

def fitness(record):
    score = 0
    
    for index, char in enumerate(record):
        if char == optiml_solution[index]:
            score += char_fit
    return score


def cross_over(parent1, parent2):
    new_record = ''
    mid_point = randint(0, len(parent1) - 1)
    new_record = parent1[0:mid_point] + parent2[mid_point:len(parent2)]
    return new_record

def mutation(record):
    r = ''
    for index, val in enumerate(record):
        if randint(1, 99) < (mutation_percentage):
            r += full_EN_char_list[randint(0, len(full_EN_char_list) - 1)]
        else:
            r += val
    return r
    
def selection(population, scores):
    selected_parents = []
    for index, val in enumerate(population):
        for i in range(floor(scores[index])):
            selected_parents.append(val)
   
    return selected_parents

def populate():
    sol = solution or init_pop
    scores = [0 for x in sol]

    new_pop = []
    for index, val in enumerate(sol):
        x = fitness(val)
        scores[index] = x
        
    selected_parents = selection(sol, scores)
    
    for i in range(0, pop_num): 
       selected_parents_len = len(selected_parents) or 0
       new_record = cross_over(selected_parents[randint(0, selected_parents_len - 1)], selected_parents[randint(0, selected_parents_len - 1)])
       highest_score(new_record)

       new_record = mutation(new_record)
       print(new_record)
       highest_score(new_record)
       new_pop.append("".join(new_record))

    return new_pop

def highest_score(record):
    global _highest_score
    global _highest_score_record 
    score = fitness(record)
    if score > _highest_score:
        _highest_score = score
        _highest_score_record = record
    return _highest_score, _highest_score_record    


def main():
    global solution
    for i in range(0, iterations):
        print(i)
        solution = populate()
        if _highest_score_record == optiml_solution:
            print("_highest_score:", _highest_score)
            print("_highest_score_record:", _highest_score_record)
            print("population number:", i)
            print("mutation rate:", mutation_percentage)
            print("# of tries: ", (i*pop_num), " / ", (pow(len(full_EN_char_list),len(optiml_solution))))
            return _highest_score, _highest_score_record 
        
    print("highest score:", _highest_score)
    print("highest score_record:", _highest_score_record)
    print("population number:", iterations)
    print("mutation rate:", mutation_percentage)
    print("# of tries: ", (i*pop_num), " / ", (pow(len(full_EN_char_list),len(optiml_solution))))
    return _highest_score,_highest_score_record

main()