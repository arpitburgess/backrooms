# this is a bubble sort program

array = [5,4,7,6,3,3,1]

def bubble_sort(array):
    for i in range(0, len(array)):
        firstnumber = 0
        secondnumber = 1
        for j in range(0, len(array)):
            if secondnumber == len(array):
                break
            elif array[firstnumber] > array[secondnumber]:
                buffer1 = array[firstnumber]
                buffer2 = array[secondnumber]
                array[firstnumber] = buffer2
                array[secondnumber] = buffer1
                firstnumber = firstnumber + 1
                secondnumber = secondnumber + 1
            else:
                firstnumber = firstnumber + 1
                secondnumber = secondnumber + 1


bubble_sort(array)
print(array)
