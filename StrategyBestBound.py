from Strategy import Strategy
from Node import Node
from utils import *
import time

"""
Brand and Bound 
"""
class StrategyBestBound(Strategy):

    def __init__(self):
        pass

    def knapsack(self, w, list_items,mesure_time):
        list_items.sort()
        TOL = 0.00000001
        """
        Las listas en python tienen métodos para ser tratadas como colas FIFO:
        insert(0, ele)-->inserta
        pop()-->extrae
        son dos de ellos
        """
        queue = []
        # pivotes
        u = Node(-1, 0, 0, 0)
        # --------
        queue.insert(0, u)
        max_profit = 0  # beneficio máximo
        solution = Node(-1, 0, 0, 0)
        #minimo = minItemWeight(list_items)
        #minimo = min(list_items)
        """
        Uno por uno extrae un elemento del árbol de decisión
        calcula el beneficio de todos los hijos del elemento extraído
        y modifica maxProfit
        """
        start = time.time()
        while queue:
            v = Node(-1, 0, 0, 0)
            u = queue.pop()
            if solution.profit < u.profit and u.weight <= w:
                solution = u
            mesure = time.time()-start
            if mesure_time-mesure<TOL:
                print("FIN")
                break
            if u.level == -1:  # el nivel incial es 0
                v.level = 0
            if u.level == len(list_items) - 1:
                continue  # continua si ya no se puede avanzar
            """
            Si no es el último nodo, entonces incrementa el nivel,
            y calcula el beneficio de los nodos hijos.
            """
            v.level = u.level + 1
            v.weight = u.weight + list_items[v.level].weight
            v.profit = u.profit + list_items[v.level].value

            """
            Si el peso acumulado es menor que W y
            el beneficio es mayor que el beneficio anterior,
            actualizar maxprofit
            """
            if v.weight <= w and v.profit > max_profit:
                max_profit = v.profit
            """
            Obtiene el límite superior del beneficio para decidir si añadir v a la cola o no.
            """
            # Para el derecho(1)
            v.bound = bound(v, w, list_items)
            if v.bound > max_profit and v.weight <= w:
                queue.insert(0, Node(v.level, v.profit, v.bound, v.weight, father=u,taken=1))
            # Para el izquierdo(0)
            v.weight = u.weight
            v.profit = u.profit
            v.bound = bound(v, w, list_items)
            if v.bound > max_profit and v.weight <= w:
                queue.insert(0, Node(v.level, v.profit, v.bound, v.weight, father=u))

            queue.sort()
        return solution
