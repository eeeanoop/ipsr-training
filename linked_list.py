class LinkedListNode:
    # Class members
    # data -> holds data of that node
    # prev -> pointer to the previous node
    # next -> pointer to the next node
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
# Linked List
# LinkedListNodes connected together
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node




if __name__ == '__main__':
    sample_data = 3
    doubly_link_list = DoublyLinkedList()
    doubly_link_list.append(3)
    doubly_link_list.append(4)
    while doubly_link_list.tail is not None:
        print(f'Node data:{doubly_link_list.}')
