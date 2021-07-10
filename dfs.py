from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# A function to do preorder tree traversal
def printPreorder(root, x):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop()
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.right),
            queue.append(node.left)

        if node.data == x:
            return


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.left = Node("F")
root.right.right = Node("G")
root.left.left = Node("D")
root.left.right = Node("E")
root.left.left.left = Node("G")
root.left.left.right = Node("H")
root.left.right.left = Node("I")
root.left.right.right = Node("K")
root.left.right.left.left = Node("K")
root.left.right.left.right = Node("L")
print("Path to node in breadth first search:")
print("Please enter which node to search for -")
x = input()
printPreorder(root, x)
