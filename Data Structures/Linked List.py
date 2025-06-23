class LinkedList:
    def __init__(self, maximum_length) -> None:
        self.maximum = maximum_length
        self.length = 0
        self.array = [None for _ in range(maximum_length)]
        self.pointers = [None for _ in range(maximum_length)]
        self.start_pointer = -1
        self.free_node_index = -1

    def traverse(self) -> None:
        print(self.start_pointer)
        print(self.array)
        print(self.pointers)
        current_pointer = self.start_pointer
        while current_pointer != -1:
            current_element = self.array[current_pointer]
            print(current_element, end=" -> ")
            current_pointer = self.pointers[current_pointer]
        print("end")

    def get_free_node_index(self) -> int:
        try:
            self.free_node_index = self.array.index(None)
            return self.free_node_index
        except:
            print("No free nodes")
            return -1

    def insert(self, element) -> bool:
        if self.length >= self.maximum:
            print("error: list is full")
            return False
        else:
            self.get_free_node_index()
            if self.start_pointer == -1:
                self.array[0], self.pointers[0] = element, -1
                self.start_pointer = 0
            elif element <= self.array[self.start_pointer]:
                self.array[self.free_node_index] = element
                self.pointers[self.free_node_index] = self.start_pointer
                self.start_pointer = self.free_node_index
            else:
                current_pointer = self.start_pointer
                target_pointer = -1
                while current_pointer != -1:
                    if element >= self.array[current_pointer]:
                        self.array[self.free_node_index] = element
                        self.pointers[self.free_node_index] = self.pointers[
                            current_pointer
                        ]
                        target_pointer = current_pointer
                    current_pointer = self.pointers[current_pointer]
                self.pointers[target_pointer] = self.free_node_index
            self.length += 1
            return True

    def delete(self, element) -> bool:
        if self.length <= 0:
            print("Error: List is empty")
        else:
            try:
                target_node_index = self.array.index(element)
                if target_node_index == self.start_pointer:
                    start_pointer_index = self.start_pointer
                    self.start_pointer = self.pointers[self.start_pointer]
                    (
                        self.array[start_pointer_index],
                        self.pointers[start_pointer_index],
                    ) = (None, None)
                else:
                    prev_node_index = self.pointers.index(target_node_index)
                    self.pointers[prev_node_index] = self.pointers[target_node_index]
                    self.pointers[target_node_index] = None
                    self.array[target_node_index] = None

            except ValueError as e:
                print(f"Element {element} was not found in the list: {e}")


if __name__ == "__main__":
    length = input("Length of linked list: ")
    linked_list = LinkedList(int(length))
    while True:
        command = input("enter command (type 'help' for help): ")
        if command == "":
            pass
        else:
            match command.split()[0].lower():
                case "help":
                    print(
                        """help: Prints this message
                        insert <element>: Inserts element into the correct position
                        delete <element>: Deletes first instance of the element
                        traverse: Traverses the linked list
                        quit/exit: exit the program"""
                    )
                case "insert":
                    linked_list.insert(command.split()[1])
                case "delete":
                    linked_list.delete(command.split()[1])
                case "traverse":
                    linked_list.traverse()
                case "quit":
                    break
                case "exit":
                    break
                case _:
                    print("enter valid command (type 'help' for list of commands)")
