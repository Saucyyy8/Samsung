import person_dao

class Person_service:
    def __init__(self):
        self.oprs = person_dao.Db_operations()

    def create_person(self):
        self.oprs.insert_row()

    def delete_person(self):
        self.oprs.delete_row()

    def update_person(self):
        self.oprs.update_row()

    def search_person(self):
        self.oprs.search_row()

    def list_all_persons(self):
        self.oprs.list_all_rows()