class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        return None
    

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        return None
    
    def push(self, value):
        """
        Add a new node to the stack.

        Keyword Arguments:
            - value: The value of the stack's new top.
        """
        new_node = Node(value)
        # Check if stack is empty
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        """
        Remove and return the top node from the stack.
        """
        # Check if stack is empty
        if self.height == 0:
            return None
        else:
            deleted_node = self.top
            self.top = self.top.next
            deleted_node.next = None
            self.height -= 1
            return deleted_node
    
    def __str__(self) -> str:
        temp = self.top
        stack_str = "[ "
        while temp != None:
            stack_str += str(temp.value) + " "
            temp = temp.next
        stack_str += "]"
        return stack_str