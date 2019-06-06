from gurobipy import *


def bound(node, w, list_items):
    if node.weight >= w:
        return 0
    estimate = node.profit
    j = node.level + 1
    total_weigth = node.weight
    while j < len(list_items) and total_weigth + list_items[j].weight <= w:
        total_weigth = total_weigth + list_items[j].weight
        estimate = estimate + list_items[j].value
        j = j + 1
    if j < len(list_items): estimate = estimate + (w - total_weigth) * list_items[j].value / list_items[j].weight
    return estimate

def output(value,taken):
    """
    General print for all solution
    :param value:
    :param taken:
    :return String:
    """
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

"""
Some Algoritms for the knapsack problem
"""

def greedy(items,capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0] * len(items)

    for i in range(len(items)):
        if weight + items[i].weight <= capacity:
            taken[i] = 1
            value += items[i].value
            weight += items[i].weight

    # prepare the solution in the specified output format
    return output(value,taken)

def solver_tab(value, weight,items,n):
    if n ==0 or weight==0:
        return 0
    return

def solver_iter (weigth,value,capacity):
    v =[[0 for x in range(capacity)] for y in range(len(value))]
    for i in range(len(value)):
        for w in range(capacity):
            if weigth[i] <= w:
                if (value[i] + v[i-1][w-weigth[i]]) > v[i-1][w]:
                    v[i][w] = value[i] + v[i-1][w-weigth[i]]
                else:
                    v[i][w] = v[i-1][w]
            else:
                v[i][w] = v[i - 1][w]
    return v

def sum_value(value,taken):
    return sum([chosen for chosen,ischosen in zip(value,taken) if ischosen == 1])

def sum_items(items,taken):
    return sum([chosen.value for chosen,ischosen in zip(items,taken) if ischosen == 1])

def dynamic_programming(items,capacity):
    weigth = []
    value = []
    for i in range(len(items)):
        value.append(items[i].value)
        weigth.append(items[i].weight)
    taken = [0]*len(value)
    v = solver_iter(weigth,value, capacity)
    i = len(value)- 1
    k = capacity-1
    while i > 0 and k > 0:
        if v[i][k] != v[i-1][k]:
            taken[i] = 1
            k = k - weigth[i]+1
            i = i -1
        else:
            taken[i] = 0
            i = i - 1
    cost=0
    for i in range(len(value)):cost+=value[i]*taken[i]
    return output(int(cost),taken)


def gurobi(items,capacity):
    taken = [0]*len(items)
    m = Model("kp")
    m.setParam('OutputFlag',False)
    for i in range(len(taken)):
        taken[i] = m.addVar(vtype=GRB.BINARY, name="x" + str(i))
    m.update()
    m.addConstr(quicksum(taken[i]*items[i].weight for i in range(len(items)))<=capacity)
    m.setObjective(quicksum(taken[i]*items[i].value for i in range(len(items))),GRB.MAXIMIZE)
    m.optimize()
    solution = []
    for v in m.getVars():
        solution.append(int(v.x))
    return output(int(m.objVal),solution)
