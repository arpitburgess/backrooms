# this is an insertion sort program
array = [1, 7, 6, 23, 1, 314513, 453]
print(array)

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j -1] > array[j] and j > 0:
            array[j -1], array[j] = array[j], array[j-1]
            j = j - 1
            print(array)

insertion_sort(array)
print(array)