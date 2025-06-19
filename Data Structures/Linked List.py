class LinkedList:
    def __init__(self, max_length):
        self.array = [None for _ in range(max_length)]
        self.pointers = [None for _ in range(max_length)]
        self.start_pointer = 4  # -1
        self.max_length = max_length
        self.length = 0
        self.free_node_index = -1
        # for testing purposes
        for i, test_element in enumerate([23, 10, 87, 22, 0]):
            self.array[i] = test_element
        for i, test_pointer in enumerate([2, 3, -1, 0, 1]):
            self.pointers[i] = test_pointer

    def traverse(self):
        print(self.array)
        print(self.pointers)
        print(self.start_pointer)
        current_pointer = self.start_pointer
        while current_pointer != -1:
            current_element = self.array[current_pointer]
            print(current_element, end=" -> ")
            current_pointer = self.pointers[current_pointer]
        print("end")

        print("\n")

    def get_index(self, element: int) -> int:
        # Aim is to get the correct node to be updated
        current_pointer = self.start_pointer
        while current_pointer != -1:
            current_element = self.array[current_pointer]
            # element needs to be behind the current element
            # index func used cuz all pointers are unique
            if current_element >= element:
                # check if element should be the first one
                if current_pointer == self.start_pointer:
                    return self.start_pointer
                return self.pointers.index(current_pointer)

            current_pointer = self.pointers[current_pointer]
        for i in range(len(self.pointers)):
            if self.pointers[i] == -1:
                return i

    def insert(self, element):
        if self.length == self.max_length:
            print("Error: linked list is full")
            return None

        pointer = self.get_index(element)
        print("pointer: ", pointer)

        self.free_node_index = -1
        for i in range(len(self.array)):
            if self.array[i] == None:  # First empty array
                self.free_node_index = i
                break
        self.array[self.free_node_index] = element


        if pointer == self.start_pointer:
            self.pointers[self.free_node_index] = self.start_pointer

        else:
            self.pointers[self.free_node_index] = self.pointers[pointer]
            self.pointers[pointer] = self.free_node_index
            return 0


if __name__ == "__main__":
    my_list = LinkedList(10)
    my_list.traverse()
    # print(my_list.get_index(21))
    my_list.insert(90)
    my_list.traverse()
