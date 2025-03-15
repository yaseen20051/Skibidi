from Scripts.Sorter import Sorter
from Scripts.MergeSort import MergeSort
from Scripts.InsertionSorting import InsertionSorting

class HypridSorting (MergeSort, InsertionSorting):
    def __init__(self):
        self.arr = []
        self.size = 0
        self.threshold = 10

    def Sort(self):
        self.arr = self.hypridSort(self.arr)
        return self.arr

    def hypridSort(self, arr):
        if len(arr) <= self.threshold:
            return self.insertionSort(arr)
        left = self.hypridSort(arr[:len(arr) // 2])
        right = self.hypridSort(arr[len(arr) // 2:])
        return self.merge(left, right)

    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)
    def set_threshold(self, threshold):
        if threshold <= 1:
            self.threshold = 1
            return
        self.threshold = threshold