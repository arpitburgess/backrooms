#this program initiates a simple linear search

#making of the array
array = [1, 3123,513,46, 5,7124561,547245,73467,3568356,7245 ,61,453]
found = 0

value = int(input("please enter the value to look for"))
for i in range(0, len(array)):
    if array[i] == value:
        print("value is found in the array")
        found = 1
        break
    else:
        pass

if found == 0:
    print("the value was not found")