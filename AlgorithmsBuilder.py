from StrategyBestBound import StrategyBestBound
class AlgorithmsBuider(object):
    def __init__(self):
        self.strategy = None

    def builderBestBoundSolution(self):
        self.strategy= StrategyBestBound()

    def knapsack(self,w,list_items,mesure_time = 5): #5 segundos
        if self.strategy != None:
            return self.strategy.knapsack(w,list_items,mesure_time)
        else:
            return None