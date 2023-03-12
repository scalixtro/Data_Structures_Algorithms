from linked_list import Node, LinkedList


def append_test() -> None:
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    print(my_linked_list.get(3).value)


def insert_test() -> None:
    my_linked_list = LinkedList(1)
    my_linked_list.append(3)

    print('LL before insert():')
    print(my_linked_list)

    my_linked_list.insert(1,2)

    print('\nLL after insert(2) in middle:')
    print(my_linked_list)

    my_linked_list.insert(0,0)

    print('\nLL after insert(0) at beginning:')
    print(my_linked_list)

    my_linked_list.insert(4,4)

    print('\nLL after insert(4) at end:')
    print(my_linked_list)


def remove_test():
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    print('LL before remove():')
    print(my_linked_list)

    print('\nRemoved node:')
    print(my_linked_list.remove(2).value)
    print('LL after remove() in middle:')
    print(my_linked_list)

    print('\nRemoved node:')
    print(my_linked_list.remove(0).value)
    print('LL after remove() of first node:')
    print(my_linked_list)

    print('\nRemoved node:')
    print(my_linked_list.remove(2).value)
    print('LL after remove() of last node:')
    print(my_linked_list)


def reverse_test():
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    print(my_linked_list)

    print('LL before reverse():')
    print(my_linked_list)

    my_linked_list.reverse()

    print('\nLL after reverse():')
    print(my_linked_list)


if __name__ == '__main__':
    reverse_test()