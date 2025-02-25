from Scripts.BubbleSorting import *
from Scripts.SelectionSorting import *
from Scripts.InsertionSorting import *
from Scripts.ArrayGenerator import *
if __name__ == '__main__':

    generator =  ArrayGenerator()
    arr = generator.GenerateArray(5)
    bubble_sorter = BubbleSorting(arr)
    print("Sorted array by bubble_sorter:", bubble_sorter.Sort())
    arr2 = generator.GenerateArray(10)
    insertion_sorter = InsertionSorting(arr2)
    print("Sorted array by insertion_sorter:", insertion_sorter.Sort())
    arr3 = generator.GenerateArray(13)
    selection_sorter = SelectionSorting(arr3)
    print("Sorted array by selection_sorter:", selection_sorter.Sort())




