class Node:
    """
    Class that implements the Node of a linked list.

    Attributes:
        value: value of the node.
        next: pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    This class is an implementation of a linked list data structure.
    """
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def append(self, value) -> bool:
        """
        Append a Node at the end of the linked list

        Keyword Arguments:
            - value: The value that the appended node will have.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value: int) -> bool:
        """
        Add a node at the beginning of the linked list

        Keyword Arguments:
            - value: The value of the new node
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        if self.tail is None:
            self.tail = self.head

        return True

    def pop(self):
        """
        Remove the last node from the linked list.
        """
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = Node(self.head.value)
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        pre = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        """
        Remove the first node from the linked list.
        """
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
        return temp

    def get(self, index: int):
        """
        Returns the node at a given index. If index is out of range
        (index <= 0 or index  > length) returns None.

        Keyword Arguments:
            - index: Index of a node in the linked list.
        """
        if index < 0 or index >= self.length:
            return None
        current_index = 0
        node_at_index = self.head
        for _ in range(index):
            node_at_index = node_at_index.next
        return node_at_index
    
    def set_value(self, index, value):
        """
        Change the value of the node at given index. 
        If there is no node at 'index', returns None.

        Keyword Arguments:
            - index: The index of the node which value will change
            . value: The new value of the node at index
        """
        node_at_index = self.get(index)
        if node_at_index is None:
            return None
        else:
            node_at_index.value = value
        return True
    
    def insert(self, index, value):
        """
        Insert a new node at given index

        Keyword Arguments:
            - index: The index that the new node will have
            - value: Value of the new node
        """
        # Check if index is valid
        if index < 0 or index > self.length:
            return False
        # Use prepend or append if index is at the begginning or end
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        # If index is valid
        previous = self.head
        node_at_index = self.head
        new_node = Node(value=value)

        for _ in range(index):
            previous = node_at_index
            node_at_index = node_at_index.next

        previous.next = new_node
        new_node.next = node_at_index
        self.length += 1

        return True
    
    def remove(self, index: int):
        # Check if index is out of range
        if index < 0 or index >= self.length:
            return None
        # Use prevoiusly defined methods
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        # If index is in the middle
        previous = self.get(index - 1)
        node_at_index = previous.next
        previous.next = node_at_index.next
        node_at_index.next = None
        self.length -= 1
        return node_at_index
    
    def reverse(self):
        # If linked list is empty or has at most 2 elements
        # Reverse head and tail
        self.head, self.tail = self.tail, self.head
        p1 = None
        p2 = self.tail
        p3 = self.tail.next
        for _ in range(self.length):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return True
    
    def __str__(self):
        temp = self.head
        list_as_str = "[ "

        while temp != None:
            list_as_str += str(temp.value) + " "
            temp = temp.next
        
        return list_as_str + "]"
    