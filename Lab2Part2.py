from Scripts.BubbleSorting import *
from Scripts.MeasureTime import MeasureTime
from Scripts.QuickSort import *
from Scripts.MergeSort import *
from Scripts.HeapSorting import *
from Scripts.PartitionSearch import QuickSearch
from Scripts.ArrayGenerator import *
import time
from Scripts.HypridSort import HypridSorting
import matplotlib.pyplot as plt

if __name__ == '__main__':

    generator = ArrayGenerator()
    hybrid = HypridSorting()
    hybrid.set_threshold(10)
    arr = generator.GenerateArray(10040)
    quicksearch = QuickSearch(arr)
    hybrid.set_arr(arr.copy())
    print(hybrid.Sort())
    print(quicksearch.search(0, len(arr)-1, 10))

