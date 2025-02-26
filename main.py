from Scripts.BubbleSorting import *
from Scripts.MeasureTime import MeasureTime
from Scripts.SelectionSorting import *
from Scripts.InsertionSorting import *
from Scripts.ArrayGenerator import *
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':

    generator =  ArrayGenerator()
    bubble_Sorter = BubbleSorting([])
    selection_Sorter = SelectionSorting([])
    insertion_sorter = InsertionSorting([])
    sizes = [1000, 5000, 10000,15000,20000]
    bubble_times,selection_times,insertion_times = [],[],[]
    for size in sizes:
        arr = generator.GenerateArray(size)

        bubble_Sorter.set_arr(arr.copy())
        insertion_sorter.set_arr(arr.copy())
        selection_Sorter.set_arr(arr.copy())

        bubble_times.append(MeasureTime.measureTime(bubble_Sorter))
        selection_times.append(MeasureTime.measureTime(selection_Sorter))
        insertion_times.append(MeasureTime.measureTime(insertion_sorter))

    plt.figure(figsize=(10, 5))

    plt.plot(sizes, bubble_times, 'bo-', label="Bubble Sort")
    plt.plot(sizes, selection_times, 'ro-', label="Selection Sort")
    plt.plot(sizes, insertion_times, 'yo-', label="Insertion Sort")

    plt.xlabel("Input Size (N)")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Sorting Algorithm Time Complexity Comparison")
    plt.legend()
    plt.grid()
    plt.show()
