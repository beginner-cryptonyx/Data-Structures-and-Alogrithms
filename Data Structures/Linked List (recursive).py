class Node:
    def __init__(self, value:int):
        self.val:int = value
        self.pointer:Node|None = None
        
    def traverse(self) -> None:
        print(self.val, end=" -> ")
        if self.pointer:
            self.pointer.traverse()
        else:
            print("end")
    
    def insert(self, value:int) -> None:
        prevNode = self
        inserted = False
        node = Node(value)
        while not inserted:
            if not prevNode.pointer:
                prevNode.pointer = node
                inserted = True
            else:
                prevNode = prevNode.pointer
    def sorted_insert(self, value:int):
        prevNode = self
        inserted = False
        node = Node(value)
        while not inserted:
            # val is lower than root
            if self.pointer is not None:
                if value <= self.val:
                    self, node = node, self
                    node.pointer = prevNode
                    inserted = True
                    return Node
                else:
                    self.pointer = node
            elif prevNode and self.val >= value and prevNode.val < value:
                prevNode.pointer, node.pointer = node, prevNode.pointer
            else:
                prevNode = self.pointer
        return self

node = Node(7)       
for i in [5]:
    node = node.sorted_insert(i)
node.traverse()

# 4,2,5,7,3,6,3,6,0