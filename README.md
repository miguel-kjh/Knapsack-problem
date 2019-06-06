# Knapsack-problem
The problem is to put items in the backpack in such a way that the value of the items it contains is maximized and as 
long as the maximum weight (or volume) that the weight can not bear is exceeded.
The solution to the problem will be given by the sequence of variables x1, x2, ..., xn where 
the value of xi indicates how many copies will be placed in the backpack of item type i.
To structure the problem, the item class has been created, representing the objects to be chosen together with their weights and values.

Methods to solve it: dynamic programming,Branch and Bound with linear relaxation and MIP with Gurobi.
