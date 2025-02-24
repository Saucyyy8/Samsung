import sys
import person_service

class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        service = person_service.Person_service()
        while True:
            choice = int(input('\n1:AddPerson 2:DeletePerson 3:UpdatePerson 4:SearchPerson 5:ListAllPersons 6:Exit.  Your choice: '))
            self.match_user_choice(choice, service)

    def match_user_choice(self, choice, service):
        match choice:
            case 1 :
                service.create_person()
            case 2 : 
                service.delete_person()
            case 3 :
                service.update_person()
            case 4 :
                service.search_person()
            case 5 :
                service.list_all_persons()
            case 6 :
                self.end_of_program()
            case _ :
                self.invalid_choice()

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()