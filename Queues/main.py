from queue import Node, Queue

def dequeue_test() -> None:
    my_queue = Queue(1)
    my_queue.enqueue(2)
    # (2) Items - Returns 2 Node
    print(my_queue.dequeue().value)
    # (1) Item -  Returns 1 Node
    print(my_queue.dequeue().value)
    # (0) Items - Returns None
    print(my_queue.dequeue())
    return None

if __name__ == '__main__':
    dequeue_test()