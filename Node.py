
"""
Clase Nodo para la estructura de datos
    level --> Nivel del nodo en el árbol
    (coincide con el indice en la lista de items porque la altura del árbol nunca será mayor a su tamaño)
    profit --> beneficion de los nodos en la ruta desde la raíz a este
    bound --> Límite máximo de ganancia(lo que estamos buscando)
    weigth --> peso actual del recorrido
"""
class Node():
    def __init__(self,level,profit,bound, weigth, father=None, taken=0):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weigth
        self.father = father
        self.taken = taken


    def __str__(self):
        return "Nivel: " + str(self.level) + " profit: " + str(self.profit)+ " bound: " \
               + str(self.bound)+ " peso: " + str(self.weight) + " taken = " + str(self.taken)

    def __lt__(self, other):
        return self.profit < other.profit

    def __gt__(self, other):
        return self.profit > other.profit
