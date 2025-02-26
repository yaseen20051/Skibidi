from Scripts.Sorter import Sorter

 # Insertion Sort : Putting elements in the right place

 # AverageCase and WorstCase are O(n^2)

 # BestCase  = O(n)

class InsertionSorting(Sorter):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        for i in range(1, self.size):
            key = self.arr[i]
            j = i - 1


            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = key

        return self.arr

    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)


