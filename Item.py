"""
Clase item para alvacenar el peso y el valor de los items
"""
class Item():
    def __init__(self, weight, value, position):
        self.weight = weight
        self.value = value
        self.position = position
    def __repr__(self):
        return "Peso: " + str(self.weight) + " Valor: " + str(self.value) + " Posición: " + str(self.position)

    def __lt__(self, other):
        return self.value/self.weight > other.value/other.weight

    def __gt__(self, other):
        return self.value/self.weight < other.value/other.weight