import random


def quickSorting(array):
    if len(array) == 0:
        return []
    else:
        pivot = random.randint(0, len(array) - 1)
        middle = array[pivot]
        left = [i for i in array if i < middle]
        right = [i for i in array if i > middle]
        return quickSorting(left) + [middle] + quickSorting(right)


print(quickSorting([5,4,5,7,3,2,8,1]))