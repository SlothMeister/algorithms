from collections import deque


# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(root, x):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = deque()

    # Put root into queue and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        node = queue.popleft()
        print(node.data, end=" ")

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

        if node.data == x:
            return


# Driver Program to test above function

# Constructing tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")
root.left.left.left = Node("G")
root.left.left.right = Node("H")
root.left.right.left = Node("I")
root.left.right.right = Node("K")
root.left.right.left.left = Node("K")
root.left.right.left.right = Node("L")

print("Path to node in breadth first search:")
print("Please enter which node to search for -")
x = input()
printLevelOrder(root, x)
