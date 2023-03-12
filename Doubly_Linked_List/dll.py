class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        Appends a new node at the end of the DLL

        Keyword Arguments:
            - value: The value of the new node to add.
        """
        new_node = Node(value)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        """
        Removes the last node from the DLL.
        """
        # Check if list is empty
        if self.length == 0:
            return None
        elif self.length == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
        else:
            deleted_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            deleted_node.prev = None
        self.length -= 1
        return deleted_node
    
    def prepend(self, value):
        """
        Adds a new node at the beginning of the DLL.

        Keyword Arguments:
            - value: The value of the new node to add.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        """
        Delete the first element from the DLL.
        """
        if self.length < 2:
            return self.pop()
            
        deleted_node = self.head
        self.head = self.head.next
        self.head.prev = None
        deleted_node.next = None
        self.length -= 1
        return deleted_node
    
    def get(self, index):
        """
        Returns the node at a given index.
        """
        # Check if index is out of range
        if index < 0 or index >= self.length:
            return None
        # If index is in the first half of the list
        if index < self.length // 2:
            node_at_index = self.head
            for _ in range(index):
                node_at_index = node_at_index.next
        else:
            node_at_index = self.tail
            for _ in range(self.length - index - 1):
                node_at_index = node_at_index.prev
        return node_at_index
    
    def set_value(self, index, value):
        """
        Changes the value of the node at the given index.

        Keyword Arguments:
            - index: Index of the node which value is going to change.
            - value: New value of the node at index.
        """
        node_at_index = self.get(index)
        if node_at_index is not None:
            node_at_index.value = value
            return True
        else:
            return False
        
    def insert(self, index, value):
        """
        Insert a new node at index position.

        Keyword Arguments:
            - index: Index that the new node will have.
            - value: Value of the new node.
        """
        # Check if index is out of range
        if index < 0 or index > self.length:
            return None
        # Check if list is empty
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            node_at_index = self.get(index)
            previous = node_at_index.prev
            # Connect the new node to previous and node_at_index
            new_node.next = node_at_index
            new_node.prev = previous
            # Delete previous connections
            previous.next = new_node
            node_at_index.previous = new_node
            self.length += 1
        return True
    
    def remove(self, index):
        """
        Remove the node at position 'index'.

        Keyword Arguments:
            - index: Index of the node to be removed.
        """
        # Check if index is out of range
        if index < 0 or index >= self.length:
            return None
        # Reuse previously defined functions
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        # Find element at index
        node_at_index = self.get(index)
        # Create the connections between nodes previous and next
        node_at_index.prev.next = node_at_index.next
        node_at_index.next.prev = node_at_index.prev
        # Delete node connections
        node_at_index.prev = None
        node_at_index.next = None
        
        self.length -= 1
        return node_at_index

    def __str__(self):
        temp = self.head
        list_as_str = "[ "
        while temp != None:
            list_as_str += str(temp.value) + " "
            temp = temp.next
        
        return list_as_str + "]"