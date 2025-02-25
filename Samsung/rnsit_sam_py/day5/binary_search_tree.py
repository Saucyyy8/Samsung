import sys

class Node:
    def __init__(self, data = 0):
        self.left = None
        self.data = data
        self.right = None
        print(f'Node with data {data} created')

class Bst:
    def __init__(self):
        self.root = None
        print('An empty Bst is created')

    def add_node(self):
        data = int(input('Enter data of the new node: '))
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if data < temp2.data:
            temp2.left = node
        else:
            temp2.right = node

    def delete_node(self):
        data = int(input('Enter data of the node to be delete: '))
        temp1 = self.root
        temp2 = None
        while temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        # temp1 now points to node to be deleted and temp2 points to its parent.
        print(f'Node with data {temp1.data} deleted')

        if temp1 is self.root:
            if temp1.left is None and temp1.right is None:
                self.root = None
            if temp1.left is not None and temp1.right is not None:
                temp3 = temp1.right.left
                if temp3 is None:
                    temp1.right.left = temp1.left
                    self.root = temp1.right
                else:
                    while temp3.left is not None:
                        temp3 = temp3.left
                    temp3.left = temp1.left
        else:
            # CODE IT HERE

        # If node to be deleted is a leaf node:
        if temp1.left is None and temp1.right is None:            
            if temp2 is None:
                self.root = None
            elif temp2.left is temp1:
                temp2.left = None
            else:
                temp2.right = None

        # If node to be deleted has 2 children
        elif temp1.left is not None and temp1.right is not None:
            temp3 = temp1.right.left
            if temp3 is None:
                temp1.right.left = temp1.left
            else:
                while temp3.left is not None:
                    temp3 = temp3.left
                temp3.left = temp1.left
            # if root is the node being deleted
            if temp1 is self.root:
                self.root = temp1.right
            elif temp2.left is temp1:
                temp2.left = temp1.right
            else:
                temp2.right = temp1.right

        # when node to be deleted has exactly one child
        else:
            #link = return () if temp1.left temp1.left else temp1.right
            link = temp1.left # assume temp1 has left child
            if temp1.right:
                link = temp1.right
            if temp2.left is temp1:
                temp2.left = link
            else:
                temp2.right = link

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')            

    def search_node(self):
        if self.root is None:
            print('Tree is empty')
            return
        data = int(input('Enter data to be searched: '))
        temp = self.root
        level = 1
        while temp != None:
            if temp.data == data:
                print(f'Node with data {data} found at level-{level}')
                return
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
            level += 1
        print(f'Node with data {data} not found')

class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def match_user_choice(self, choice, bst):
        match choice:
            case 1 :
                bst.add_node()
            case 2 : 
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.delete_node()
            case 3 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.inorder(bst.root)
            case 4 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.preorder(bst.root)
            case 5 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.postorder(bst.root)
            case 6 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.search_node()
            case 7 :
                self.end_of_program()
            case _ :
                self.invalid_choice()

    def run_menu(self):
        bst = Bst()
        while True:
            choice = int(input('\n1:Add 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Search 7:Exit.  Your choice: '))
            self.match_user_choice(choice, bst)

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()
