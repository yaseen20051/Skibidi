class HeapSorting():

    def __init__(self):
        self.arr = []
        self.size = 0
    def BuildMaxHeap(self,arr):
         n = len(arr)
         for i in range (len(arr)//2,-1 , -1):  ## fixed from len(arr)//2 -1 to start from the first parent
             self.heapify(arr,n,i);

    def heapify(self,arr,n,index):  ## guarantee that the father is the max elemnt between his children O(lgn)
        leftChild = 2*index + 1   ## fixed from 2*index
        rightChild = 2*index + 2  ## fixed from 2*index+1
        maxIndex = index
        if (leftChild < n    and arr[leftChild]>arr[maxIndex]):
            maxIndex = leftChild
        if (rightChild< n and arr[rightChild]>arr[maxIndex]):
            maxIndex = rightChild

        if maxIndex != index:
            arr[index],arr[maxIndex] = arr[maxIndex],arr[index]
            self.heapify(arr,n,maxIndex)

    def Sort(self):
        heapSize = len(self.arr)
        self.BuildMaxHeap(self.arr)
        print(self.arr)
        for i in range (len(self.arr)-1,-1,1):
            self.arr[i],self.arr[0] =  self.arr[0],self.arr[i]
            heapSize = heapSize-1
            self.heapify(self.arr,heapSize,0)

    def get_arr(self):
        return self.arr

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)