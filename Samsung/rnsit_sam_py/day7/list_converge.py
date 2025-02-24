class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self, num):
        self.head = None
        print(f'List-{num} is created')

    def create_node(self, data):
        node = Node(data)
        return node

    def add_node_at_front(self, data):
        if self.head is None:
            self.head = self.create_node(data)
        new_node = self.create_node(data)
        new_node.link = self.head
        self.head = new_node

def create_list(num):
    list = LinkedList()
    print(f'Creating List-{num}')
    while True:
        data = input('Enter data of the new node: ')
        list.add_node_at_front(data)
        choice = input('Enter 1 to add node, other number to stop: ')
        if choice.__eq__('1'):
            break
    return list

def check_if_converges(list1, list2):
    if list1.head is None or list2.head is None:
        print('Lists do not converge')
        return
    temp1 = list1.head
    temp2 = list2.head
    count = 0
    while temp1 is not None and temp2 is not None:
        if temp1.link == temp2.link:
            return count
    return -1

list1 = create_list(1)
list2 = create_list(2)
position = check_if_converges(list1, list2)
if position == -1:
    print('The lists do not converge')
else:
    print(f'The lists converges at position-{position}')