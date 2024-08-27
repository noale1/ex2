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

def main():
    # delete later 
    # # Example usage:
    stack = None  # Start with an empty stack
    stack = push(stack, 10)
    stack = push(stack, 20)
    popped_data, stack = pop(stack)  # Pops 20
    popped_data, stack = pop(stack)  # Pops 10
    popped_data, stack = pop(stack)  # Stack is empty

if __name__ == "__main__":
    main()

