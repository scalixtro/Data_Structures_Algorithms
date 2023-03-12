class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        return None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        return None
    
    def enqueue(self, value):
        """
        Add a new node at the end of the queue.

        Keyword Arguments:
            - value: The value of the new node to add.
        """
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        """
        Remove and return the first node from the queue.
        """
        # Check if queue is empty
        deleted_node = self.first
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return deleted_node

    def __str__(self) -> str:
        temp = self.first
        queue_as_str = ""

        while temp != None:
            queue_as_str += str(temp.value) + " <- "
            temp = temp.next
        
        return queue_as_str