class Event:
    def monday(self):
        print('Today is Technical Fest')

    def tuesday(self):
        print('Today is Cultural Fest')

    def wednesday(self):
        print('Today is Sports Fest')

    def thursday(self):
        print('Today is Ethnic Fest')

    def other_day(self):
        print('Invalid choice enetered')

class Menu:
    def __init__(self):
        pass
    def get_menu(self, events):
        menu = {
            1 : events.monday,
            2 : events.tuesday,
            3 : events.wednesday,
            4 : events.thursday
        }
        return menu
    
    def run_menu(self):
        event = Event()
        while True:
            choice = int(input('1: Monday 2:Tuesday 3:Wednesday 4:Thursday. (-1 to Exit) Your choice: '))
            if choice == -1:
                break
            menu = self.get_menu(event)
            menu.get(choice, event.other_day)()
            # self.get_menu(event).get(choice, event.other_day)()
        print('End of program')
    
menu = Menu()
menu.run_menu()