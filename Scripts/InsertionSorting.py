from Scripts.Sorter import Sorter

 # Insertion Sort : Putting elements in the right place

 # AverageCase and WorstCase are O(n^2)

 # BestCase  = O(n)

class InsertionSorting(Sorter):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        self.arr = self.insertionSort(self.arr)
        return self.arr

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1


            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)


