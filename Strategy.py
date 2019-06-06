import abc
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def knapsack(self,w,list_items,mesure_time):#10 seconds
        pass