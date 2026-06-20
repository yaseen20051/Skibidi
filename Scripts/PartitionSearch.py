from Scripts.QuickSort import QuickSort

class QuickSearch():
    def __init__(self, arr):
        self.arr = arr
        self.qs = QuickSort(self.arr)

    def search(self, low, high, key):
        #Since it's 0-index based, so it's better to do the 
        #calculations inside the method 
        key-=1 

        if low <= high:
            pivotIndex = self.qs.partition(low, high)
            #print(pivotIndex)
            #If the given index is the pivot
            if pivotIndex == key:
                return self.arr[pivotIndex]
            
            elif pivotIndex < key:
                #a 1 is added to the recursive call to compensate the k-=1 
                # at the begining of each call so that the key doesn't change
                return self.search(pivotIndex + 1, high, key + 1)

            elif pivotIndex > key:
                return self.search(low, pivotIndex - 1, key + 1)
        