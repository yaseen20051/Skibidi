from Scripts.Sorter import Sorter


# Selection Sort : Putting min Elements Ahead

# AverageCase , BestCase and WorstCase are O(n^2)



class SelectionSorting(Sorter):
    def __init__(self,arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        for i in range(self.size - 1):
            min_index = i

            for j in range(i + 1, self.size):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            if min_index != i:
                self.SwapFunction(self.arr, i, min_index)

        return self.arr
    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)

