import json
import easygui
import questionary


class GetModule:
    @staticmethod
    def view_user_details(data_file_path):
        account_number = input("Enter your account number: ")

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user = None

        for user_data in data:
            if user_data['account_number'] == account_number and user_data['is_active']:
                found_user = user_data
                break

        if found_user:
            print("User details for account number", account_number)
            print("Name:", found_user['account_name'])
            print("Phone Number:", found_user['is_valid_phone_number'])
            print("Email:", found_user['email'])
            print("Address:", found_user['address'])
            print("Pincode:", found_user['is_valid_pincode'])
            print("Bank Name:", found_user['bank_name'])
            print("IFSC code:", found_user['ifsc'])
            print("Account Type:", found_user['account_type'])
            print("Total Amount:", found_user['total_amount'])
            print("Status: Active")
            print("Created At:", found_user['created_at'])
            print("Updated At:", found_user['updated_at'])
            transaction_history = found_user.get('transaction_history', [])
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(
                        f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Created at: {transaction['created_at']}")
        else:
            print("User not found")

    @staticmethod
    def view_user_details_gui(data_file_path):
        choices = ["Account Number", "Account Name", "Phone Number"]
        search_option = easygui.buttonbox(
            "How would you like to access your account?", choices=choices)

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        if search_option == "Account Number":

            account_number = input("Enter your account number: ")

            interaction_log = {
                "account number": "Enter your account number: "
            }

            user_input_details = {
                "account number": account_number
            }

            found_user = None

            for user_data in data:
                if user_data['account_number'] == account_number and user_data['is_active']:
                    found_user = user_data
                    break

            if found_user:
                print("User details for account number", account_number)
                print("Name:", found_user['account_name'])
                print("Phone Number:", found_user['phone_number'])
                print("Email:", found_user['email'])
                print("Address:", found_user['address'])
                print("Pincode:", found_user['pincode'])
                print("Bank Name:", found_user['bank_name'])
                print("IFSC code:", found_user['ifsc'])
                print("Account Type:", found_user['account_type'])
                print("Total Amount:", found_user['total_amount'])
                print("Status: Active")
                print("Created At:", found_user['created_at'])
                print("Updated At:", found_user['updated_at'])
                transaction_history = found_user.get('transaction_history', [])
                if transaction_history:
                    print("Transaction History:")
                    for transaction in transaction_history:
                        print(
                            f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Created at: {transaction['created_at']}")

                found_user_redux = found_user['account_name']

            else:
                print("User not found")

            return interaction_log, user_input_details, found_user_redux

        elif search_option == "Account Name":

            account_name = input("Enter your account name: ")

            interaction_log = {
                "account name": "Enter your account name: "
            }

            user_input_details = {
                "account number": account_name
            }

            found_user = []

            for user_data in data:
                if user_data['account_name'] == account_name and user_data['is_active']:
                    found_user.append(user_data)

            if found_user:
                for user in found_user:
                    print("\n")
                    print("User details for account number",
                          user['account_number'])
                    print("Name:", user['account_name'])
                    print("Phone Number:", user['phone_number'])
                    print("Email:", user['email'])
                    print("Address:", user['address'])
                    print("Pincode:", user['pincode'])
                    print("Bank Name:", user['bank_name'])
                    print("IFSC code:", user['ifsc'])
                    print("Account Type:", user['account_type'])
                    print("Total Amount:", user['total_amount'])
                    print("Status: Active")
                    print("Created At:", user['created_at'])
                    print("Updated At:", user['updated_at'])
                    transaction_history = user.get('transaction_history', [])
                    if transaction_history:
                        print("Transaction History:")
                        for transaction in transaction_history:
                            print(
                                f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Created at: {transaction['created_at']}")

                    found_user_redux = user['account_name']

            else:
                print("User not found")

            return interaction_log, user_input_details, found_user_redux

        elif search_option == "Phone Number":
            phone_number = input("Enter your phone number: ")

            interaction_log = {
                "phone name": "Enter your phone number: "
            }

            user_input_details = {
                "phone number": phone_number
            }

            found_user = []

            for user_data in data:
                if user_data['phone_number'] == phone_number and user_data['is_active']:
                    found_user.append(user_data)

            if found_user:
                for user in found_user:
                    print("\n")
                    print("User details for account number",
                          user['account_number'])
                    print("Name:", user['account_name'])
                    print("Phone Number:", user['phone_number'])
                    print("Email:", user['email'])
                    print("Address:", user['address'])
                    print("Pincode:", user['pincode'])
                    print("Bank Name:", user['bank_name'])
                    print("IFSC code:", user['ifsc'])
                    print("Account Type:", user['account_type'])
                    print("Total Amount:", user['total_amount'])
                    print("Status: Active")
                    print("Created At:", user['created_at'])
                    print("Updated At:", user['updated_at'])
                    transaction_history = user.get('transaction_history', [])
                    if transaction_history:
                        print("Transaction History:")
                        for transaction in transaction_history:
                            print(
                                f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Created at: {transaction['created_at']}")

                found_user_redux = user['account_name']

            else:
                print("User not found")

            return interaction_log, user_input_details, found_user_redux

    @staticmethod
    def view_user_details_questionary(data_file_path):
        choices = ["Account Number", "Account Name", "Phone Number"]
        search_option = questionary.select(
            "How would you like to access your account?", choices=choices).ask()

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        if search_option == "Account Number":

            account_number = input("Enter your account number: ")

            interaction_log = {
                "Enter your account number:": account_number
            }

            found_user = None

            for user_data in data:
                if user_data['account_number'] == account_number and user_data['is_active']:
                    found_user = user_data
                    break

            if found_user:
                user_output = found_user
                found_user_redux = found_user['account_name']

            else:
                user_output = "User not found"

            return interaction_log, user_output, found_user_redux

        elif search_option == "Account Name":

            account_name = input("Enter your account name: ")

            interaction_log = {
                "Enter your account name:": account_name
            }

            found_user = []

            for user_data in data:
                if user_data['account_name'] == account_name and user_data['is_active']:
                    found_user.append(user_data)

            if found_user:
                user_output = found_user
                for user in found_user:
                    found_user_redux = user['account_name']

            else:
                user_output = print("User not found")

            return interaction_log, found_user, found_user_redux

        elif search_option == "Phone Number":
            phone_number = input("Enter your phone number: ")

            interaction_log = {
                "Enter your phone number:": phone_number
            }

            found_user = []

            for user_data in data:
                if user_data['phone_number'] == phone_number and user_data['is_active']:
                    found_user.append(user_data)

            if found_user:
                user_output = found_user
                for user in found_user:
                    found_user_redux = user['account_name']

            else:
                user_output = print("User not found")

            return interaction_log, user_output, found_user_redux
