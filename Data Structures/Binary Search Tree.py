# One class implementation
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            elif self.right is not None:
                self.right.insert(value)

        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            elif self.left is not None:
                self.left.insert(value)

    def traverse(self, mode="inorder"):
        if mode == "preorder":
            print(self.value, end=" ")
        if self.left is not None:
            self.left.traverse(mode)
        if mode == "inorder":
            print(self.value, end=" ")
        if self.right is not None:
            self.right.traverse(mode)
        if mode == "postorder":
            print(self.value, end=" ")

    def search(self, element):
        if self.value == element:
            return self
        elif element < self.value and self.left is not None:
            return self.left.search(element)
        elif element > self.value and self.right is not None:
            return self.right.search(element)

    def delete(self, element):
        if self.search(element) is not None:
            if self.left == element:
                if self.left.left is None and self.left.right is None:
                    self.value = self.left.value
                    self.left = None
            # if self.element
                    
                

if __name__ == "__main__":
    root = BinaryTreeNode(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(14)
    root.insert(4)
    root.insert(7)
    root.insert(13)

    print("\ninorder")
    root.traverse(mode="inorder")

    print("\npreorder")
    root.traverse(mode="preorder")

    print("\npostorder")
    root.traverse(mode="postorder")

    print(root.search(15))
