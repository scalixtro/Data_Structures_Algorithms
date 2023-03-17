class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        return None
    

class BinarySearchTree:
    def __init__(self, value=None) -> None:
        if value is None:
            self.root = None
        else:
            root_node = Node(value)
            self.root = root_node
        return None
    
    def insert(self, value):
        """
        Insert a new node in the tree. If node already exists then
        returns False, otherwise returns True.

        Keyword Arguments:
            - value: The value of the new node to insert.
        """
        # Check if root is empty
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        p1 = self.root
        while True:
            if value == p1.value:
                # Node already exists
                return False
            elif value > p1.value:
                # Insert to right or move
                if p1.right is None:
                    p1.right = new_node
                    break
                p1 = p1.right
            elif value < p1.value:
                # Insert left or move
                if p1.left is None:
                    p1.left = new_node
                    break
                p1 = p1.left
        return True
    
    def contains(self, value):
        """
        Check if a given value is in the tree.

        Keyword Arguments:
            - value: Node value to look for.
        """
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def __r_contains(self, current_node, value):
        # Check if current node has the searched value or
        # is None
        if current_node is None: 
            return False
        elif current_node.value == value:
            return True
        # Navigate through the tree
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        """
        Recursively search for a given value inside the binary tree.

        Keyword Arguments:
            - value: The value to search for.
        """
        return self.__r_contains(current_node=self.root, value=value)
    
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        """
        Recursively add a new node with value 'value'. If the node already
        exists then do nothing.

        Keyword Arguments:
            - value: The value of the new node to insert.
        """
        if self.root is None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    
    def min_value(self, current_node):
        """
        Finds the minimum value within a sub-tree.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        # If current node is none, means that value is not in the tree
        if current_node is None:
            return None
        # Keep searching through the tree
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # If we found the value
        if current_node.value == value:
            # Leaf node
            if (current_node.right is None) and (current_node.left is None):
                return None
            # Node with elements on the left
            elif current_node.right is None:
                current_node = current_node.left
            # Node with elements on the right side
            elif current_node.left is None:
                current_node = current_node.right
            # Node with elements at both sides
            else:
                min_value = self.min_value(current_node.right)
                current_node.right = self.__delete_node(current_node.right, min_value)
                current_node.value = min_value
        # If we never found a node with the value, no changes are made
        return current_node
    
    def delete_node(self, value):
        """
        Deletes a Node with a given value recursively
        """
        return self.__delete_node(self.root, value)

    def BFS(self):
        """Breadth First Search algorithm"""
        current_node = self.root
        queue = []
        results = []
        if current_node is not None:
            queue.append(current_node)
        while len(queue) > 0:
            # Point to the first element in queue
            current_node = queue[0]
            # Add the element at the start of the queue and remove
            results.append(queue.pop(0).value)
            # Add left element if is not None
            if current_node.left is not None:
                queue.append(current_node.left)
            # Append right node if is not None
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        """
        Depth First Search: Recursive tree traversal Pre-Order algorithm.
        """
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        """
        Depth First Search: Recursive tree traversal Post-Order algorithm.
        """
        results = []
        
        def traverse(current_node):
            if current_node.left == None and current_node.right == None:
                results.append(current_node.value)
                return None
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        if self.root is not None:
            traverse(self.root)
        return results
    
    def dfs_in_order(self):
        """
        Depth First Search: Recursive tree traversal In-Order algorithm.
        """
        results = []
        def traverse(current_node):
            # First traverse through the left branch of a node if exists
            if current_node.left is not None:
                traverse(current_node.left)
            # Add the current node (all the right branch nodes are > node)
            results.append(current_node.value)
            # Traverse through the right branch of the node
            if current_node.right is not None:
                traverse(current_node.right)
        # Start from the root
        traverse(self.root)
        return results