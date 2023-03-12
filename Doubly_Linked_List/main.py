from dll import Node, DoublyLinkedList


def append_test() -> None:
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)


    print('Head:', my_doubly_linked_list.head.value)
    print('Tail:', my_doubly_linked_list.tail.value)
    print('Length:', my_doubly_linked_list.length, '\n')

    print('Doubly Linked List:')
    print(my_doubly_linked_list)

    return None


def pop_test() -> None:
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    # (2) Items - Returns 2 Node
    print(my_doubly_linked_list.pop().value)
    # (1) Item -  Returns 1 Node
    print(my_doubly_linked_list.pop().value)
    # (0) Items - Returns None
    print(my_doubly_linked_list.pop())
    return None


def remove_test() -> None:
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)

    print('DLL before remove():')
    print(my_doubly_linked_list)

    print('\nRemoved node:')
    print(my_doubly_linked_list.remove(2).value)
    print('DLL after remove() in middle:')
    print(my_doubly_linked_list)

    print('\nRemoved node:')
    print(my_doubly_linked_list.remove(0).value)
    print('DLL after remove() of first node:')
    print(my_doubly_linked_list)

    print('\nRemoved node:')
    print(my_doubly_linked_list.remove(2).value)
    print('DLL after remove() of last node:')
    print(my_doubly_linked_list)
    return None


if __name__ == '__main__':
    remove_test()