from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchtree:
    def __init__(self):
        self.root = Node(None)
    def insert(self, value):
        new_node = Node(value)
        if self.root.data is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if value >= current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else :
                        current_node = current_node.right
                else :
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else :
                        current_node = current_node.left
    def print_tree(self):
        # bfs method
        need_visited = deque()
        need_visited.append(self.root)
        while need_visited:
            current_node = need_visited.popleft()
            if current_node.data is not None:
                print(current_node.data, end=" ")
            if current_node.left is not None:
                need_visited.append(current_node.left)
            if current_node.right is not None:
                need_visited.append(current_node.right)
        print()
    def find(self, value):
        current_node = self.root
        if current_node.data is None:
            return False
        while True:
            if value > current_node.data:
                if current_node.right is None:
                    return False
                else:
                    current_node = current_node.right
            elif value < current_node.data:
                if current_node.left is None:
                    return False
                else:
                    current_node = current_node.left
            else:
                return True

BST = BinarySearchtree()
BST.insert(10)
BST.insert(5)
BST.insert(15)
BST.insert(3)
BST.insert(12)
BST.insert(7)
BST.print_tree()
print(BST.find(8))