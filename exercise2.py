def create_node(data):
    """Creates a new node as a tuple (data, next)."""
    return (data, None)

def push(stack, data):
    """Pushes an element onto the stack."""
    new_node = create_node(data)
    new_node = (new_node[0], stack)
    return new_node

def pop(stack):
    """Pops an element from the stack."""
    if is_empty(stack):
        print("Stack is empty. Cannot pop.")
        return None, stack
    popped_data = stack[0]
    stack = stack[1]
    print(f"Popped {popped_data} from stack.")
    return popped_data, stack

def is_empty(stack):
    """Checks if the stack is empty."""
    return stack is None

# Example usage:
stack = None  # Start with an empty stack
stack = push(stack, 10)
stack = push(stack, 20)
popped_data, stack = pop(stack)  # Pops 20
popped_data, stack = pop(stack)  # Pops 10
popped_data, stack = pop(stack)  # Stack is empty
