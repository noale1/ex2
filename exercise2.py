def createNode(data):
    return (data, None)

def push(stack, data):
    newNode = createNode(data)
    newNode = (newNode[0], stack)
    return newNode

def pop(stack):
    if isEmpty(stack):
        return None, stack
    poppedData = stack[0]
    stack = stack[1]
    return poppedData, stack

def top(stack):
    if not isEmpty(stack):
        return stack[0]
    return None

def isEmpty(stack):
    return stack is None

def createViewArray(buildingArray):
    
    # Initialize view array with zeros and create an empty stack
    viewArray = [0] * len(buildingArray)
    tempStack = []
    
    # Go over building list and find the next heighest building
    # If there is none that means the building's view is the ocean
    for i in range(len(buildingArray)):
        while tempStack and buildingArray[top(tempStack)] <= buildingArray[i]:
            _, tempStack = pop(tempStack)
            
        # If the temp stack is not empty, calculate the index for the view array
        if tempStack:
            viewArray[i] = top(tempStack) + 1
        
        # Push the current index into stack
        tempStack = push(tempStack, i)
    
    return viewArray

def main():
    buildingArray = []
    while (len(buildingArray) != 30):
        inputString = input("Please Enter a list of exactly 30 building heights (seperated by commas): ")
        buildingArray = inputString.split(",")
        buildingArray = [int(x) for x in buildingArray]
    
    outputArray = createViewArray(buildingArray)
    for i in range(len(buildingArray)):
        print("Building number " + str(i) + " : " + str(outputArray[i]) + "")
        
        
    
        

if __name__ == "__main__":
    main()