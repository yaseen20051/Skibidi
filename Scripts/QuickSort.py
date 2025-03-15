from Sorter import Sorter
import random 

#Best case O(nlogn)
#Worts case O(n^2) -> When array is sorted
class QuickSort(Sorter):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
    
    # Partition method
    def partition(self, low, high):
        #choosing pivot at random from the range of sub arrays (low, high)
        pivot = random.randint(low, high) 
        #Swap the pivot with the last element 
        self.SwapFunction(self.arr, pivot, high)
        pivot = high

        #Index that helps in placing the pivot in its right place 
        #smalller(i) -> pivot(i+1) -> greater(i+2)
        i = low - 1

        #Traversing the array to shift all elments from low to i to the right
        for j in range(low, high):
            if self.arr[j] < self.arr[pivot]:
                i+=1
                self.SwapFunction(self.arr, i, j)
        
        self.SwapFunction(self.arr, i+1, pivot)
        return i + 1
    
    #Sorting implementation
    def quickSort(self, low, high):
        if low < high:
            pivotIndex = self.partition(low, high)
            self.quickSort(low, pivotIndex - 1)
            self.quickSort(pivotIndex + 1, high)
    
    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)

    def Sort(self):
        self.quickSort(0, len(self.arr) - 1)
        return self.arr

        