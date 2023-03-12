from bst import BinarySearchTree, Node


def recursive_contains_test() -> None:
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print('BST Contains 27:')
    print(my_tree.r_contains(27)) # Expected: True

    print('\nBST Contains 17:')
    print(my_tree.r_contains(17)) # Expected: False
    return None


def recursive_insert_test() -> None:
    my_tree = BinarySearchTree()
    my_tree.r_insert(2)
    my_tree.r_insert(1)
    my_tree.r_insert(3)

    """
        THE LINES ABOVE CREATE THIS TREE:
                  2
                 / \
                1   3
    """


    print('Root:', my_tree.root.value)            
    print('Root->Left:', my_tree.root.left.value)        
    print('Root->Right:', my_tree.root.right.value)        



    """
        EXPECTED OUTPUT:
        ----------------
        Root: 2
        Root->Left: 1
        Root->Right: 3

    """
    return None


def min_value_test() -> None:
    list_nums = [21, 76, 18, 27, 52, 82]
    my_tree = BinarySearchTree(47)
    """
    Create a tree:
             47
           /    \
          21    76
         / \    / \
        18 27  52 82
    """
    for num in list_nums:
        my_tree.r_insert(num)
    print("TREE CREATED")
    print("""         
             47
           /    \\
          21    76
         / \    / \\
        18 27  52 82\n""")
    print("Minimum value from root: ", my_tree.min_value(my_tree.root))
    print("Minimum value from root.right: ", my_tree.min_value(my_tree.root.right))
    return None

def delete_test() -> None:
    list_nums = [21, 76, 18, 27, 52, 82]
    my_tree = BinarySearchTree(47)
    """
    Create a tree:
             47
           /    \
          21    76
         / \    / \
        18 27  52 82
    """
    for num in list_nums:
        my_tree.r_insert(num)
    print("TREE CREATED")
    print("""         
             47
           /    \\
          21    76
         / \    / \\
        18 27  52 82\n""")
    # Delete 76 node
    my_tree.delete_node(76)
    print("76 in Tree: ", my_tree.contains(76))
    print("\nRight subtree")
    print("""         
             47
           /    \\
          21    82
         / \    / \\
        18 27  52 \n""")
    print("Right node: ", my_tree.root.right.value)
    print("Right-node.left",  my_tree.root.right.left.value)
    print("Right-node.right",  my_tree.root.right.right)
    return None


if __name__ == '__main__':
    delete_test()