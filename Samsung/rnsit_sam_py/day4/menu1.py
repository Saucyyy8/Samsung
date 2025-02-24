def monday():
    print('Today is Technical Fest')

def tuesday():
    print('Today is Cultural Fest')

def wednesday():
    print('Today is Sports Fest')

def thursday():
    print('Today is Ethnic Fest')

def other_day():
    print('Invalid choice enetered')

menu = {
    1 : monday,
    2 : tuesday,
    3 : wednesday,
    4 : thursday
}

while True:
    choice = int(input('1: Monday 2:Tuesday 3:Wednesday 4:Thursday. (-1 to Exit) Your choice: '))
    if choice == -1:
        break
    menu.get(choice, other_day)()
print('End of program')