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

def createNewStack(inputStack):
    # Extract data into an array format from the input stack
    dataArray = [data for _, data in inputStack if data is not None]

    # Initialize the output array with 0s and a stack to assist with index calculation
    outputArray = [0] * len(dataArray)
    stack = []

    # Traverse the data_array from left to right
    for i in range(len(dataArray)):
        # Maintain a stack of indices in decreasing order of their values
        while stack and dataArray[stack[-1]] <= dataArray[i]:
            stack.pop()

        # If stack is not empty, calculate the index for the output_array
        if stack:
            outputArray[i] = stack[-1] + 1

        # Push current index onto the stack
        stack.append(i)

    # Create the output stack based on the output_array
    outputStack = [(None, outputArray[0])]  # Start with the first node

    for i in range(1, len(outputArray)):
        outputStack.append((outputArray[i - 1], outputArray[i]))

    outputStack.append((outputArray[-1], None))  # Add the last node

    return outputStack


def main():
    inputStack = [(None, 101), (101, 87), (87, 122), (208, 74), (74, 107), (107, 152), (152, 130), (130, None)]
    outputStack = createNewStack(inputStack)
    print(outputStack)
    

if __name__ == "__main__":
    main()

