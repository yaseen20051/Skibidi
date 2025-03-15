from Scripts.Sorter import Sorter

# Bubble Sort : Swapping elements untill being Swapped

# AverageCase and WorstCase are O(n^2)

# BestCase  = O(n)

class MergeSort (Sorter):
    def __init__(self):
        self.arr = []
        self.size = 0


    def Sort(self):
        self.arr = self.mergeSort(self.arr)
        return self.arr


    def mergeSort(self, array):
        if len(array) == 1:
            return array
        left = self.mergeSort(array[:len(array) // 2])
        right = self.mergeSort(array[len(array) // 2:])
        return self.merge(left, right)
    def merge(self, array1, array2):
        i = o = 0
        merged = []
        while i < len(array1) and o < len(array2):
            if array1[i] < array2[o]:
                merged.append(array1[i])
                i += 1
            else:
                merged.append(array2[o])
                o += 1
        while i < len(array1):
            merged.append(array1[i])
            i += 1
        while o < len(array2):
            merged.append(array2[o])
            o += 1
        return merged
    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)