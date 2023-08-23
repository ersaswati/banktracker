import json
import easygui


class DeleteModule:
    @staticmethod
    def delete_user(data_file_path):
        account_number = input(
            "Enter Account Number of User You Want To Delete: ")

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user_data = None
        for user_data in data:
            if user_data['account_number'] == account_number:
                found_user_data = user_data
                break

        if found_user_data:
            confirm = input("Are you sure you want to delete? (Y/N): ").upper()

            if confirm == 'Y':
                found_user_data['is_active'] = False
                with open(data_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                print("Deleted Successfully!!")
            else:
                print("Data not deleted")
        else:
            print("user not found")

    @staticmethod
    def delete_user_2(data_file_path):
        account_number = input(
            "Enter Account Number of User You Want To Delete: ")

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user_data = None
        for user_data in data:
            if user_data['account_number'] == account_number:
                found_user_data = user_data
                break

        if found_user_data:
            choices = ["Yes", "No"]
            confirm = easygui.buttonbox(
                "Are you sure you want to delete?", choices=choices)

            if confirm == 'Yes':
                found_user_data['is_active'] = False
                with open(data_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                print("Deleted Successfully!!")
            else:
                print("Data not deleted")
        else:
            print("user not found")

        interaction_log = {
            "accout number": "Enter Account Number of User You Want To Delete: ",
            "confirm": "Are you sure you want to delete?"
        }

        user_input_details = {
            "account number": account_number,
            "confirm": confirm
        }

        return interaction_log, user_input_details
