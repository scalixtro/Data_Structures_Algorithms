from stack import Node, Stack

def pop_test() -> None:
    my_stack = Stack(4)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)

    print('Stack before pop():')
    print(my_stack)

    print('\nPopped node:')
    print(my_stack.pop().value)

    print('\nStack after pop():')
    print(my_stack)
    return None

if __name__ == "__main__":
    pop_test()