firstlist = [0,0,0,0,0]
frontpointer = 0
rearpointer = -1
queuefull = 5
queuelength = 0
def enqueue(value):
    global queuelength, rearpointer
    if queuelength < queuefull:
        if rearpointer == 4:
           rearpointer = 0
        else:
            rearpointer = rearpointer + 1
        queuelength = queuelength + 1
        firstlist[rearpointer] = value
    else:
        print("queue is full")
def dequeue():
    global queuelength, frontpointer
    if queuelength == 0:
        print("queue is empty")
    else:
        if frontpointer == 4:
            frontpointer = 0
        else:
            frontpointer = frontpointer + 1
        queuelength = queuelength - 1
def displayqueue():
    if rearpointer <= frontpointer:
        for i in range(frontpointer, 5):
            print(firstlist[i])
        for i in range(0, frontpointer + 1):
            print(firstlist[i])
    else:
        for i in range(frontpointer, rearpointer + 1):
            print(firstlist[i])
while True:
    userinput = input("1. Enqueue \n2.Dequeue\n3.Display Queue\n4.Exit")
    if userinput == "1":
        uservalue = input("what value would you like to add to the queue")
        enqueue(uservalue)
    elif userinput == "2":
        dequeue()
    elif userinput == "3":
        displayqueue()
    elif userinput == "4":
        exit()