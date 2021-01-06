class Node:
    """Represents a node in a singly linked list
    Attributes:
        __data (int): data stored inside the node
        __next_node (Node): next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """Initializes the node
        Args:
            data (int): data stored inside the node
            next_node (Node): next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of __data
        Returns:
            data stored inside the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data
        Args:
            value (int): data stored insite the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of __next_node
        Returns:
           the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node
        Args:
            value (Node): next node in the linked list
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """Represents a single linked list
    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """Initializes the linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position
        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """
        new = Node(value)
        temp = self.__head
        if temp is None or temp.data >= value:
            if temp:
                new.next_node = temp
            self.__head = new
            return
        while temp.next_node is not None:
            if temp.next_node.data >= value:
                break
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        """String representation of SinglyLinkedList instance
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            if temp.next_node is not None:
                string += "\n"
            temp = temp.next_node
        return string
