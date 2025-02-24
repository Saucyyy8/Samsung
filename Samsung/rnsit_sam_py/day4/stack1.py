import sys

class Stack:
    def __init__(self, size=5):
        self.stk = []
        self.size = size
        print('Empty Stack is created')
    
    def push(self):
        if len(self.stk) == self.size:
            print('Stack is full')
            return
        element = input('Enter the element to be pushed: ')
        self.stk.insert(0, element)

    def pop(self):
        if not self.stk:
            print('Stack is empty')
            return
        print(f'Popped element is {self.stk[0]}')
        del self.stk[0]

    def list_stack(self):
        if not self.stk:
            print('Stack is empty')
            return
        print('The Stack is \n', self.stk) # stk[::-1]

class Menu:
    def get_menu(self, stack):
        menu = {
            1 : stack.push,
            2 : stack.pop,
            3 : stack.list_stack,
            4 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        stack = Stack()
        while True:
            choice = int(input('1: Push 2:Pop 3:Display 4:Exit. Your choice: '))
            menu = self.get_menu(stack)
            menu.get(choice, self.invalid_choice)()
    
menu = Menu()
menu.run_menu()