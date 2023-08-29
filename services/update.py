import json
import datetime
import easygui
import questionary


class TransactionHistory():
    def __init__(self, account_number):
        self.account_number = account_number
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "transaction_type": transaction_type,
            "amount": amount,
            "created_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions


class UpdateModule:
    @staticmethod
    def update_user_details(data_file_path):
        account_number = input("Enter the account number you want to update: ")

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user_data = None
        for user_data in data:
            if user_data['account_number'] == account_number:
                if user_data['is_active']:
                    found_user_data = user_data
                    break

        if found_user_data is not None:
            while True:
                update_choice = input(
                    "Enter 'U' to update user details, 'W' to withdraw money, 'D' to deposit money, or 'Q' to quit: ").upper()
                if update_choice == 'U':
                    while True:
                        update_choice_2 = input(
                            "Enter 'N' to update name, 'E' to update e-mail, 'A' to update your address, 'P' to update pincode, 'PN' to update phone number, or 'Q' to quit: ").upper()
                        if update_choice_2 == 'N':
                            name = input("Enter the name you want to update: ")
                            found_user_data['account_name'] = name
                        elif update_choice_2 == 'E':
                            email = input(
                                "Enter the email you want to update: ")
                            found_user_data['email'] = email
                        elif update_choice_2 == 'A':
                            address = input(
                                "Enter the address you want to update: ")
                            found_user_data['address'] = address
                        elif update_choice_2 == 'P':
                            pincode = input(
                                "Enter the pincode you want to update: ")
                            found_user_data['is_valid_pincode'] = pincode
                        elif update_choice_2 == 'PN':
                            phone_number = input(
                                "Enter the phone number you want to update: ")
                            found_user_data['is_valid_phone_number'] = phone_number
                        elif update_choice_2 == 'Q':
                            updated_at = datetime.datetime.now()
                            found_user_data['updated_at'] = updated_at.strftime(
                                '%Y-%m-%d %H:%M:%S')
                            with open(data_file_path, 'w') as json_file:
                                json.dump(data, json_file, indent=4)

                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif update_choice == 'W':
                    withdrawal_amount = float(
                        input("Enter the amount to withdraw: "))

                    if withdrawal_amount <= found_user_data['total_amount']:
                        found_user_data['total_amount'] -= withdrawal_amount
                        transaction_history = TransactionHistory(
                            account_number)
                        transaction_history.add_transaction(
                            "Withdrawal", withdrawal_amount)
                        if 'transaction_history' in found_user_data:
                            found_user_data['transaction_history'].extend(
                                transaction_history.transactions)
                        else:
                            found_user_data['transaction_history'] = transaction_history.transactions
                        updated_at = datetime.datetime.now()
                        found_user_data['updated_at'] = updated_at.strftime(
                            '%Y-%m-%d %H:%M:%S')
                        with open(data_file_path, 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        print("Withdrawal successful, Total amount:",
                              found_user_data['total_amount'])
                    else:
                        print("Insufficient balance!")

                elif update_choice == 'D':
                    deposit_amount = float(
                        input("Enter the amount to deposit: "))

                    found_user_data['total_amount'] += deposit_amount
                    transaction_history = TransactionHistory(account_number)
                    transaction_history.add_transaction(
                        "Deposit", deposit_amount)
                    if 'transaction_history' in found_user_data:
                        found_user_data['transaction_history'].extend(
                            transaction_history.transactions)
                    else:
                        found_user_data['transaction_history'] = transaction_history.transactions
                    updated_at = datetime.datetime.now()
                    found_user_data['updated_at'] = updated_at.strftime(
                        '%Y-%m-%d %H:%M:%S')
                    with open(data_file_path, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    print("Deposit successful. Total amount:",
                          found_user_data['total_amount'])

                elif update_choice == 'Q':
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("User not found")

    @staticmethod
    def update_user_details_gui(data_file_path):
        account_number = input("Enter the account number you want to update: ")

        interaction_log = {
            "account number": "Enter the account number you want to update: "
        }

        user_input_details = {
            "account number": account_number
        }

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user_data = None
        for user_data in data:
            if user_data['account_number'] == account_number:
                if user_data['is_active']:
                    found_user_data = user_data
                    break

        if found_user_data is not None:
            while True:
                update_choices = ["Update User Details",
                                  "Withdraw Money", "Deposit Money", "Quit"]
                update_choice = easygui.buttonbox(
                    "What do you want to do?", choices=update_choices)

                interaction_log["choice 1"] = "What do you want to do?"
                user_input_details["choice 1"] = update_choice

                if update_choice == 'Update User Details':
                    while True:
                        update_choices_2 = [
                            "Name", "Email", "Address", "Pincode", "Phone Number", "Quit"]
                        update_choice_2 = easygui.buttonbox(
                            "What do you want to update?", choices=update_choices_2)

                        interaction_log["choice 2"] = "What do you want to update?"
                        user_input_details["choice 2"] = update_choice_2

                        if update_choice_2 == 'Name':
                            name = input("Enter the new name:")
                            found_user_data['account_name'] = name

                            interaction_log["new name"] = "Enter the new name:"
                            user_input_details["new name"] = name

                        elif update_choice_2 == 'Email':
                            email = input(
                                "Enter the new email: ")
                            found_user_data['email'] = email

                            interaction_log["new email"] = "Enter the new email:"
                            user_input_details["new email"] = email

                        elif update_choice_2 == 'Address':
                            address = input(
                                "Enter the new address:")
                            found_user_data['address'] = address

                            interaction_log["new address"] = "Enter the new address:"
                            user_input_details["new address"] = address

                        elif update_choice_2 == 'Pincode':
                            pincode = input(
                                "Enter the new pincode:")
                            found_user_data['pincode'] = pincode

                            interaction_log["new pincode"] = "Enter the new pincode:"
                            user_input_details["new pincode"] = pincode

                        elif update_choice_2 == 'Phone Number':
                            phone_number = input(
                                "Enter the new phone number:")
                            found_user_data['phone_number'] = phone_number

                            interaction_log["new phone number"] = "Enter the new phone number:"
                            user_input_details["new phone number"] = phone_number

                        elif update_choice_2 == 'Quit':
                            updated_at = datetime.datetime.now()
                            found_user_data['updated_at'] = updated_at.strftime(
                                '%Y-%m-%d %H:%M:%S')
                            with open(data_file_path, 'w') as json_file:
                                json.dump(data, json_file, indent=4)

                            break

                elif update_choice == 'Withdraw Money':
                    withdrawal_amount = float(
                        input("Enter the amount to withdraw: "))

                    interaction_log["withdrawal amount"] = "Enter the amount to withdraw:"
                    user_input_details["withdrawal amount"] = withdrawal_amount

                    if withdrawal_amount <= found_user_data['total_amount']:
                        found_user_data['total_amount'] -= withdrawal_amount
                        transaction_history = TransactionHistory(
                            account_number)
                        transaction_history.add_transaction(
                            "Withdrawal", withdrawal_amount)
                        if 'transaction_history' in found_user_data:
                            found_user_data['transaction_history'].extend(
                                transaction_history.transactions)
                        else:
                            found_user_data['transaction_history'] = transaction_history.transactions
                        updated_at = datetime.datetime.now()
                        found_user_data['updated_at'] = updated_at.strftime(
                            '%Y-%m-%d %H:%M:%S')
                        with open(data_file_path, 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        print("Withdrawal successful, Total amount:",
                              found_user_data['total_amount'])
                    else:
                        print("Insufficient balance!")

                elif update_choice == 'Deposit Money':
                    deposit_amount = float(
                        input("Enter the amount to deposit: "))

                    interaction_log["deposit amount"] = "Enter the amount to deposit:"
                    user_input_details["deposit amount"] = deposit_amount

                    found_user_data['total_amount'] += deposit_amount
                    transaction_history = TransactionHistory(account_number)
                    transaction_history.add_transaction(
                        "Deposit", deposit_amount)
                    if 'transaction_history' in found_user_data:
                        found_user_data['transaction_history'].extend(
                            transaction_history.transactions)
                    else:
                        found_user_data['transaction_history'] = transaction_history.transactions
                    updated_at = datetime.datetime.now()
                    found_user_data['updated_at'] = updated_at.strftime(
                        '%Y-%m-%d %H:%M:%S')
                    with open(data_file_path, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    print("Deposit successful. Total amount:",
                          found_user_data['total_amount'])

                elif update_choice == 'Quit':
                    break

        else:
            print("User not found")

        return interaction_log, user_input_details

    @staticmethod
    def update_user_details_questionary(data_file_path):
        account_number = input("Enter the account number you want to update: ")

        interaction_log = {
            "Enter the account number you want to update:": account_number
        }

        with open(data_file_path) as json_file:
            data = json.load(json_file)

        found_user_data = None
        for user_data in data:
            if user_data['account_number'] == account_number:
                if user_data['is_active']:
                    found_user_data = user_data
                    break

        if found_user_data is not None:
            while True:
                update_choices = ["Update User Details",
                                  "Withdraw Money", "Deposit Money", "Quit"]
                update_choice = questionary.select(
                    "What do you want to do?", choices=update_choices).ask()

                interaction_log["What do you want to do?"] = update_choice

                if update_choice == 'Update User Details':
                    while True:
                        update_choices_2 = [
                            "Name", "Email", "Address", "Pincode", "Phone Number", "Quit"]
                        update_choice_2 = questionary.select(
                            "What do you want to update?", choices=update_choices_2).ask()

                        interaction_log["What do you want to update?"] = update_choice_2

                        if update_choice_2 == 'Name':
                            name = input("Enter the new name:")
                            found_user_data['account_name'] = name

                            interaction_log["Enter the new name:"] = name

                        elif update_choice_2 == 'Email':
                            email = input(
                                "Enter the new email: ")
                            found_user_data['email'] = email

                            interaction_log["Enter the new email:"] = email

                        elif update_choice_2 == 'Address':
                            address = input(
                                "Enter the new address:")
                            found_user_data['address'] = address

                            interaction_log["Enter the new address:"] = address

                        elif update_choice_2 == 'Pincode':
                            pincode = input(
                                "Enter the new pincode:")
                            found_user_data['pincode'] = pincode

                            interaction_log["Enter the new pincode:"] = pincode

                        elif update_choice_2 == 'Phone Number':
                            phone_number = input(
                                "Enter the new phone number:")
                            found_user_data['phone_number'] = phone_number

                            interaction_log["Enter the new phone number:"] = phone_number

                        elif update_choice_2 == 'Quit':
                            updated_at = datetime.datetime.now()
                            found_user_data['updated_at'] = updated_at.strftime(
                                '%Y-%m-%d %H:%M:%S')
                            with open(data_file_path, 'w') as json_file:
                                json.dump(data, json_file, indent=4)

                            break

                elif update_choice == 'Withdraw Money':
                    withdrawal_amount = float(
                        input("Enter the amount to withdraw: "))

                    interaction_log["Enter the amount to withdraw:"] = withdrawal_amount

                    if withdrawal_amount <= found_user_data['total_amount']:
                        found_user_data['total_amount'] -= withdrawal_amount
                        transaction_history = TransactionHistory(
                            account_number)
                        transaction_history.add_transaction(
                            "Withdrawal", withdrawal_amount)
                        if 'transaction_history' in found_user_data:
                            found_user_data['transaction_history'].extend(
                                transaction_history.transactions)
                        else:
                            found_user_data['transaction_history'] = transaction_history.transactions
                        updated_at = datetime.datetime.now()
                        found_user_data['updated_at'] = updated_at.strftime(
                            '%Y-%m-%d %H:%M:%S')
                        with open(data_file_path, 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        print("Withdrawal successful, Total amount:",
                              found_user_data['total_amount'])
                    else:
                        print("Insufficient balance!")

                elif update_choice == 'Deposit Money':
                    deposit_amount = float(
                        input("Enter the amount to deposit: "))

                    interaction_log["Enter the amount to deposit:"] = deposit_amount

                    found_user_data['total_amount'] += deposit_amount
                    transaction_history = TransactionHistory(account_number)
                    transaction_history.add_transaction(
                        "Deposit", deposit_amount)
                    if 'transaction_history' in found_user_data:
                        found_user_data['transaction_history'].extend(
                            transaction_history.transactions)
                    else:
                        found_user_data['transaction_history'] = transaction_history.transactions
                    updated_at = datetime.datetime.now()
                    found_user_data['updated_at'] = updated_at.strftime(
                        '%Y-%m-%d %H:%M:%S')
                    with open(data_file_path, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    print("Deposit successful. Total amount:",
                          found_user_data['total_amount'])

                elif update_choice == 'Quit':
                    break

        else:
            print("User not found")

        return interaction_log
