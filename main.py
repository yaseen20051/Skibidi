from Scripts.BubbleSorting import *
from Scripts.MeasureTime import MeasureTime
from Scripts.SelectionSorting import *
from Scripts.InsertionSorting import *
from Scripts.QuickSort import *
from Scripts.MergeSort import *
from Scripts.HeapSorting import *
from Scripts.ArrayGenerator import *
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':

    generator =  ArrayGenerator()
    bubble_Sorter = BubbleSorting([])
    selection_Sorter = SelectionSorting([])
    insertion_sorter = InsertionSorting([])
    quickSort = QuickSort([])
    mergeSort = MergeSort()
    heapSort = HeapSorting()
    sizes = [1000, 5000, 10000, 15000, 20000]
    QuickSort, MergeSort, HeapSort = [], [], []
    bubble_times,selection_times,insertion_times = [],[],[]
    for size in sizes:
        arr = generator.GenerateArray(size)

        bubble_Sorter.set_arr(arr.copy())
        insertion_sorter.set_arr(arr.copy())
        selection_Sorter.set_arr(arr.copy())

        bubble_times.append(MeasureTime.measureTime(bubble_Sorter))
        selection_times.append(MeasureTime.measureTime(selection_Sorter))
        insertion_times.append(MeasureTime.measureTime(insertion_sorter))

        quickSort.set_arr(arr.copy())
        heapSort.set_arr(arr.copy())
        mergeSort.set_arr(arr.copy())

        QuickSort.append(MeasureTime.measureTime(quickSort))
        MergeSort.append(MeasureTime.measureTime(mergeSort))
        HeapSort.append(MeasureTime.measureTime(heapSort))

    plt.figure(figsize=(20, 10))


    plt.plot(sizes, bubble_times, 'bo-', label="Bubble Sort")
    plt.plot(sizes, selection_times, 'ro-', label="Selection Sort")
    plt.plot(sizes, insertion_times, 'yo-', label="Insertion Sort")

    plt.plot(sizes, QuickSort, 'go-', label="Quick sort")
    plt.plot(sizes, MergeSort, 'mo-', label="Merge sort")
    plt.plot(sizes, HeapSort, 'ko-', label="Heap sort")

    plt.xlabel("Input Size (N)")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Sorting Algorithm Time Complexity Comparison")
    plt.legend()
    plt.grid()
    plt.show()

    print("\nExecution Times for Sorting Algorithms:\n")
    print(f"{'Input Size (N)':<15}{'Bubble Sort (ms)':<20}{'Selection Sort (ms)':<20}{'Insertion Sort (ms)':<20}{'Quick sort (ms)':<20}{'Merge sort (ms)':<20}{'Heap sort (ms)':<20}")
    print("=" * 150)

    for i in range(len(sizes)):
        print(f"{sizes[i]:<15}{bubble_times[i]:<20.2f}{selection_times[i]:<20.2f}{insertion_times[i]:<20.2f}{sizes[i]:<15}{QuickSort[i]:<20.2f}{MergeSort[i]:<20.2f}{HeapSort[i]:<20.2f}")

    print("\n◆ Running time for Bubble Sort, Selection Sort, Insertion Sort, Quick sort, Merge sort, and Heap sort is printed above.")

