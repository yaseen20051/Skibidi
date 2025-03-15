class HeapSorting():


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

    def Sort(self,arr):
        heapSize = len(arr)
        self.BuildMaxHeap(arr)
        print(arr)
        for i in range (len(arr)-1,-1,1):
            arr[i],arr[0] =  arr[0],arr[i]
            heapSize = heapSize-1
            self.heapify(arr,heapSize,0)
