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

def isEmpty(stack):
    return stack is None

def createNewStack(buildingStack):
    # Change stack into array 
    dataArray = []
    for _, data in buildingStack:
        if data is not None:
            dataArray.append(data)
        
    # Initialize the output array (with zeros) and initialize stack
    viewArray = []
    for _ in range(len(dataArray)):
        viewArray.append(0)
    stack = []

    # Switch dataArray from left to right
    for i in range(len(dataArray)):
        while stack and dataArray[stack[-1]] <= dataArray[i]:
            stack.pop()
        if stack:
            viewArray[i] = stack[-1] + 1
        stack.append(i)

    # Create the view stack based on the dataArray
    viewStack = [(None, viewArray[0])]  
    for i in range(1, len(viewArray)):
        viewStack.append((viewArray[i - 1], viewArray[i]))
    viewStack.append((viewArray[-1], None))  

    return viewStack


def main():
    buildingStack = [(None, 101), (101, 87), (87, 122), (208, 74), (74, 107), (107, 152), (152, 130), (130, None)]
    viewStack = createNewStack(buildingStack)
    print(viewStack)
    

if __name__ == "__main__":
    main()

