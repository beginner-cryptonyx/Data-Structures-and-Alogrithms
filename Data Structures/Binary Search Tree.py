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

    def __inorder(self):
        if self.left is not None:
            self.left.__inorder()
        print(self.value)
        if self.right is not None:
            self.right.__inorder()

    def traverse(self, mode: str = "inorder"):
        match mode:
            case "inorder":
                self.__inorder()


if __name__ == "__main__":
    root = BinaryTreeNode(20)
    root.insert(34)
    root.insert(1)
    root.insert(3)
    root.insert(234)
    root.insert(323)
    root.insert(123)
    root.insert(45)
    root.insert(26)

    root.traverse(mode="inorder")
    
