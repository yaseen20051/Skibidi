from Scripts.BubbleSorting import *
from Scripts.MeasureTime import MeasureTime
from Scripts.QuickSort import *
from Scripts.MergeSort import *
from Scripts.HeapSorting import *
from Scripts.ArrayGenerator import *
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':

    generator = ArrayGenerator()
    quickSort = QuickSort([])
    mergeSort = MergeSort()
    heapSort = HeapSorting()
    sizes = [1000, 5000, 10000, 15000, 20000]
    QuickSort,MergeSort,HeapSort = [],[],[]
    
    for size in sizes:
        arr = generator.GenerateArray(size)

        quickSort.set_arr(arr.copy())
        heapSort.set_arr(arr.copy())
        mergeSort.set_arr(arr.copy())

        QuickSort.append(MeasureTime.measureTime(quickSort))
        MergeSort.append(MeasureTime.measureTime(mergeSort))
        HeapSort.append(MeasureTime.measureTime(heapSort))

    plt.figure(figsize=(10, 5))


    plt.plot(sizes, QuickSort, 'bo-', label="Quick sort")
    plt.plot(sizes, MergeSort, 'ro-', label="Merge sort")
    plt.plot(sizes, HeapSort, 'yo-', label="Heap sort")

    plt.xlabel("Input Size (N)")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Sorting Algorithm Time Complexity Comparison")
    plt.legend()
    plt.grid()
    plt.show()

    print("\nExecution Times for Sorting Algorithms:\n")
    print(f"{'Input Size (N)':<15}{'Quick sort (ms)':<20}{'Merge sort (ms)':<20}{'Heap sort (ms)':<20}")
    print("=" * 75)

    for i in range(len(sizes)):
        print(f"{sizes[i]:<15}{QuickSort[i]:<20.2f}{MergeSort[i]:<20.2f}{HeapSort[i]:<20.2f}")

    print("\n◆ Running time for Quick sort, Merge sort, and Heap sort is printed above.")


## Latex Report Link : https://www.overleaf.com/4977366428ymwxgwtsmvrd#a97b77