from Scripts.Sorter import Sorter

# Bubble Sort : Swapping elements untill being Swapped

# AverageCase and WorstCase are O(n^2)

# BestCase  = O(n)

class BubbleSorting (Sorter):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)


    def Sort(self):

        is_sorted = True
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.SwapFunction(self.arr, j, j + 1)
                    is_sorted = False
            if is_sorted:
                break
        return self.arr

    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)

