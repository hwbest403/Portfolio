class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node(None)
    def addlist(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    def deletenode(self, idx):
        target = 0
        prev_node = self.head
        if prev_node.next is None:
            return print("List is Empty")
        next_node = prev_node.next
        while next_node.next is not None and target != idx:
            next_node = next_node.next
            prev_node = prev_node.next
            target += 1
        prev_node.next = next_node.next
        return print(f"{idx}th node delete, value : {next_node.data}")
    def find(self, value):
        current_node = self.head
        idx = -1
        while current_node is not None:
            if current_node.data == value:
                return print(f"Node at {idx}")
            current_node = current_node.next
            idx += 1
        return print("Node not found")
    def size(self):
        current_node = self.head
        res = 0
        while current_node.next:
            current_node = current_node.next
            res += 1
        return print(f"size : {res}")
    def printlist(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            print(current_node.data, end=" ")
        print()

ls1 = Linked_List()
ls1.addlist(1)
ls1.addlist(2)
ls1.addlist(3)
ls1.addlist(4)
ls1.printlist()
ls1.find(1)
ls1.deletenode(0)
ls1.find(1)
ls1.printlist()
ls1.size()