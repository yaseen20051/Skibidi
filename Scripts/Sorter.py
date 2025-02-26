from abc import ABC,abstractmethod
   # ABC stands for Abstract base class
class Sorter(ABC):  # Abstract class

    @abstractmethod
    def Sort(self):
            pass
    def SwapFunction(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i];
