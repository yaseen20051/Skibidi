import random

# Create an array of numbers from 1 to 100
class ArrayGenerator():

    def GenerateArray(self,size):

            arr = [random.randint(1, 100) for _ in range(size)]
            random.shuffle(arr)
           # print(arr)
            # print(arr)
            return arr

