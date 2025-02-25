from Scripts.Sorter import Sorter


class InsertionSorting(Sorter):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        for i in range (1,self.size):
                # print("i = ",i)
            for j in range (0,i):

                # print("j = ", j)
                if(self.arr[i]<self.arr[j]):
                    self.SwapFunction(self.arr,i,j)
        return self.arr




