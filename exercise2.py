def create_node(data):
    return (data, None)

def push(stack, data):
    new_node = create_node(data)
    new_node = (new_node[0], stack)
    return new_node

def pop(stack):
    if is_empty(stack):
        return None, stack
    popped_data = stack[0]
    stack = stack[1]
    return popped_data, stack

def is_empty(stack):
    return stack is None

def create_new_stack(input_stack):
    # Extract data into an array format from the input stack
    data_array = [data for _, data in input_stack if data is not None]

    # Initialize the output array with 0s and a stack to assist with index calculation
    output_array = [0] * len(data_array)
    stack = []

    # Traverse the data_array from left to right
    for i in range(len(data_array)):
        # Maintain a stack of indices in decreasing order of their values
        while stack and data_array[stack[-1]] <= data_array[i]:
            stack.pop()

        # If stack is not empty, calculate the index for the output_array
        if stack:
            output_array[i] = stack[-1] + 1

        # Push current index onto the stack
        stack.append(i)

    # Create the output stack based on the output_array
    output_stack = [(None, output_array[0])]  # Start with the first node

    for i in range(1, len(output_array)):
        output_stack.append((output_array[i - 1], output_array[i]))

    output_stack.append((output_array[-1], None))  # Add the last node

    return output_stack


def main():
    input_stack = [(None, 101), (101, 87), (87, 122), (208, 74), (74, 107), (107, 152), (152, 130), (130, None)]
    output_stack = create_new_stack(input_stack)
    print(output_stack)

    

if __name__ == "__main__":
    main()

