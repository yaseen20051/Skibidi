from Scripts.Sorter import Sorter
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
        #Swap the pivot with the first element 
        self.SwapFunction(self.arr, pivot, low)
        pivot = low

        #Index that helps in placing the pivot in its right place 
        #pivot(low) -> smalller(1:lastS1) -> greater(firstUnkown:high)
        lastS1 = low
        fisrtUnkown = low + 1

        #Traversing the array to shift all elments from low to lastS1 to high
        for fisrtUnkown in range(low + 1, high + 1):
            if self.arr[fisrtUnkown] < self.arr[pivot]:
                lastS1+=1
                self.SwapFunction(self.arr, fisrtUnkown, lastS1)
        
        self.SwapFunction(self.arr, lastS1, pivot)
        return lastS1
    
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


        