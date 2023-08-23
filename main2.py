import os
import json
import easygui
from services.insert import InsertModule
from services.get import GetModule
from services.update import UpdateModule
from services.delete import DeleteModule


class MainBankSystem:
    def __init__(self, data_file_path, log_file_path=None):
        self.data_file_path = data_file_path
        self.log_file_path = log_file_path
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'w') as json_file:
                json.dump([], json_file, indent=4)
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'w') as log_file:
                json.dump([], log_file, indent=4)

    def log_interaction(self, user_input, system_output, user_data=None):
        with open(self.log_file_path, 'r') as log_file:
            logs = json.load(log_file)
        log_entry = {"user_input": user_input, "system_output": system_output}
        if user_data:
            log_entry["user_data"] = user_data
        logs.append(log_entry)
        with open(self.log_file_path, 'w') as log_file:
            json.dump(logs, log_file, indent=4)

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

    def main2(self):
        insert_module = InsertModule()
        get_module = GetModule()
        update_module = UpdateModule()
        delete_module = DeleteModule()

        while True:
            choices = ["Create New Account", "View User Details",
                       "Update User Details", "Delete User", "Quit"]
            choice = easygui.buttonbox(
                "What do you want to do?", choices=choices)

            if choice == 'Create New Account':
                interaction_log, user_input_details = insert_module.create_account_2(
                    self.data_file_path)
                self.log_interaction(
                    "Create New Account", interaction_log, user_data=user_input_details)

            elif choice == 'View User Details':
                interaction_log, user_input_details = get_module.view_user_details_2(
                    self.data_file_path)
                self.log_interaction(
                    "View User Details", interaction_log, user_data=user_input_details)

            elif choice == 'Update User Details':
                interaction_log, user_input_details = update_module.update_user_details_2(
                    self.data_file_path)
                self.log_interaction(
                    "Update User Details", interaction_log, user_data=user_input_details)

            elif choice == 'Delete User':
                interaction_log, user_input_details = delete_module.delete_user_2(
                    self.data_file_path)
                self.log_interaction(
                    "Delete User", interaction_log, user_data=user_input_details)

            elif choice == 'Quit':
                self.quit()
                break

    def quit(self):
        print("You quit successfully")


if __name__ == "__main__":
    data_file_path = "data.json"
    log_file_path = "interaction_log.json"
    bank_system = MainBankSystem(data_file_path, log_file_path)
    bank_system.main2()
