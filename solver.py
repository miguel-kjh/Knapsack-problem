#!/usr/bin/python3.6
import time
import sys
from Item import Item
from AlgorithmsBuilder import AlgorithmsBuider
from utils import *

def solve_it (input_data,es="",end=0):
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    itmes = []
    for i in range(item_count):
        line = lines[i+1]
        parts = line.split()

        itmes.append(Item(int(parts[1]),int(parts[0]),i))
    if es == "bb":
        print("Best Bound Solution")
        st = time.time()
        alg = AlgorithmsBuider()
        alg.builderBestBoundSolution()
        solution = alg.knapsack(capacity, itmes,end)
        maxprofit = solution.profit
        taken = [0 for _ in range(len(itmes))]
        itmes.sort()
        while solution.father != None:
            if solution.taken == 1:
                taken[itmes[solution.level].position] = 1
            solution = solution.father
        medida_tiempo = time.time() - st
        print("Tiempo %f s" % medida_tiempo)
        return output(int(maxprofit), taken)
    elif es == "pd":
        print("Dynamic programming Solution")
        return dynamic_programming(itmes,capacity)
    elif es == "gb":
        print("Gurobi Solution")
        return gurobi(itmes,capacity)
    elif es == "gr":
        print("Greedy Solution")
        return greedy(itmes, capacity)
    #Solucion por defecto
    return gurobi(itmes,capacity)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        if len(sys.argv) > 2:
            es = sys.argv[2].strip()
        else:
            es = ""
        end = 5
        if len(sys.argv) > 3 and sys.argv[3].strip() == "-t":
            end = sys.argv[4].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data,es,int(end)))

    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
