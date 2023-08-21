import os
import json
from services.insert import InsertModule
from services.get import GetModule
from services.update import UpdateModule
from services.delete import DeleteModule

class MainBankSystem:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'w') as json_file:
                json.dump([], json_file, indent=4)

    def main(self):
        insert_module = InsertModule()
        get_module = GetModule()
        update_module = UpdateModule()
        delete_module = DeleteModule()

        while True:
            choice = input(
                "Enter 'A' to create a new account, 'V' to view user details, 'U' to update user details, 'D' to delete, or 'Q' to quit: ").upper()

            if choice == 'A':
                insert_module.create_account(self.data_file_path)
            elif choice == 'V':
                get_module.view_user_details(self.data_file_path)
            elif choice == 'U':
                update_module.update_user_details(self.data_file_path)
            elif choice == 'D':
                delete_module.delete_user(self.data_file_path)
            elif choice == 'Q':
                self.quit()
                break
            else:
                print("Invalid choice")

    def quit(self):
        print("You quit successfully")

if __name__ == "__main__":
    data_file_path = "data.json"
    bank_system = MainBankSystem(data_file_path)
    bank_system.main()
