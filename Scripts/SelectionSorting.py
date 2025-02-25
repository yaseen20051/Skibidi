from Scripts.Sorter import Sorter

class SelectionSorting(Sorter):
    def __init__(self,arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        for i in range (self.size-1):
            minIndex,min = self.GetMin(i)
            self.arr.pop(minIndex)
            self.arr.insert(i,min)
        return self.arr

    def GetMin(self,start):
        min = self.arr[start]
        minIndex = start
        for i in range (start,self.size):
            if self.arr[i]<min:
                minIndex = i
                min = self.arr[i]
        return minIndex,min



