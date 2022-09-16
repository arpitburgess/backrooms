#this is a stack program which can do push and pop

stack = [0,
         0,
         0,
         0,
         0]
toppointer = 5

def push(stack, value):
    global toppointer
    if toppointer == 0:
        print("stack is full cannot push value")
    else:
        toppointer = toppointer - 1
        stack[toppointer] = value
    print(stack)

def pop(stack):
    if stack[toppointer] == 5:
        print("no values left to pop")
    else:
        stack[toppointer] = 0
    print(stack)


push(stack, 12)
push(stack, 2)
pop(stack)