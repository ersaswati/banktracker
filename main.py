import datetime
import re
import json
import random
import os
from collections import OrderedDict


class BankUser():
    def __init__(self, name, account_number, is_valid_phone_number, email, address, is_valid_pincode, account_type, bank_name, ifsc, total_amount, is_active=True):
        self.account_name = name
        self.account_number = account_number
        self.is_valid_phone_number = is_valid_phone_number
        self.is_valid_pincode = is_valid_pincode
        self.email = email
        self.address = address
        self.bank_name = bank_name
        self.ifsc = ifsc
        self.account_type = account_type
        self.total_amount = total_amount
        self.is_active = is_active
        self.created_at = datetime.datetime.now()
        self.updated_at = None

    def to_ordered_dict(self):
        return OrderedDict([
            ("account_name", self.account_name),
            ("account_number", self.account_number),
            ("phone_number", self.phone_number),
            ("pincode", self.pincode),
            ("email", self.email),
            ("address", self.address),
            ("bank_name", self.bank_name),
            ("ifsc", self.ifsc),
            ("account_type", self.account_type),
            ("total_amount", self.total_amount),
            ("is_active", self.is_active),
            ("created_at", self.created_at.strftime('%Y-%m-%d %H:%M:%S')),
            ("updated_at", self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
             ) if self.updated_at else ("updated_at", "Not updated")
        ])


data_file_path = "data.json"
if not os.path.exists(data_file_path):
    with open(data_file_path, 'w') as json_file:
        json.dump([], json_file, indent=4)

    with open(data_file_path) as json_file:
        data = json.load(json_file)
    users = []


class TransactionHistory():
    def __init__(self, account_number):
        self.account_number = account_number
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "transaction_type": transaction_type,
            "amount": amount,
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions


class MainBankSystem():
    def __init__(self):
        self.data = []
        self.data_file_path = "data.json"
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'w') as json_file:
                json.dump([], json_file, indent=4)

        with open(self.data_file_path) as json_file:
            file_content = json_file.read()
            self.data = json.loads(file_content)

    @staticmethod
    def is_valid_phone_number(phone_number):
        return len(str(phone_number)) == 10 and str(phone_number).isdigit()

    @staticmethod
    def is_valid_pincode(pincode):
        return len(str(pincode)) == 5 and str(pincode).isdigit()

    def save_data(self):
        with open(self.data_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

    def main(self):
        while True:
            choice = input(
                "Enter 'A' to create a new account, 'V' to view user details, 'U' to update user details, 'D' to delete, 'W' to withdraw, 'DPT' to deposit, or 'Q' to quit: ").upper()

            if choice == 'A':
                self.create_account()
            elif choice == 'V':
                self.view_user_details()
            elif choice == 'U':
                self.update_user_details()
            elif choice == 'D':
                self.delete_user()
            elif choice == 'W':
                self.withdraw_amount()
            elif choice == 'DPT':
                self.deposit_amount()
            elif choice == 'Q':
                self.quit()
                break
            else:
                print("invalid choice")

    def create_account(self):
        mainsystem_instance = MainBankSystem()
        name = input("Enter your full name: ")
        account_number = str(random.randint(1000000000, 9999999999))
        print("Your Account Number:", account_number)
        while True:
            phone_number = input("Enter your phone number: ")
            if mainsystem_instance.is_valid_phone_number(phone_number):
                break
            print(
                "Phone number should be exactly 10 digits long and consist of digits only. Please re-enter.")
        while True:
            pincode = input("Enter your pincode: ")
            if mainsystem_instance.is_valid_pincode(pincode):
                break
            print(
                "Pincode should be exactly 5 digits long and consist of digits only. Please re-enter.")
        email = input("Enter your e-mail ID: ")
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            print("Invalid email address. Please enter a valid email.")
        address = input("Enter your address: ")
        bank_name = input("Enter your bank_name: ")
        ifsc = input("Enter your IFSC code: ")
        account_type = input("Enter your account_type: ")
        total_amount = 0
        created_at = datetime.datetime.now()

        bank_account = BankUser(name, account_number, phone_number, email, address,
                                pincode, account_type, bank_name, ifsc, total_amount, is_active=True)
        bank_account.created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')
        users.append(bank_account)
        self.data.append(bank_account.__dict__)
        with open(self.data_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        print("User added successfully!")

    def view_user_details(self):
        account_number = input("Enter your account number: ")
        found_user = None

        for user_data in self.data:
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
            transaction_history = TransactionHistory(account_number)
            if 'transaction_history' in found_user:
                transaction_history.transactions = found_user['transaction_history']
                print("Transaction History:")
                for transaction in transaction_history.get_transaction_history():
                    print(
                        f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Timestamp: {transaction['timestamp']}")
        else:
            print("User not found")

    def update_user_details(self):
        account_number = input("Enter the account number you want to update: ")
        found_user_index = None
        for index, user_data in enumerate(self.data):
            if user_data['account_number'] == account_number:
                if user_data['is_active']:
                    found_user_index = index
                    break

        if found_user_index is not None:
            found_user_data = self.data[found_user_index]
            while True:
                update_choice = input(
                    "Enter 'N' to update name, 'E' to update e-mail, 'A' to update your address, 'P' to update pincode, 'PN' to update phone number, or 'Q' to quit: ").upper()
                if update_choice == 'N':
                    name = input("Enter the name you want to update: ")
                    found_user_data['account_name'] = name
                elif update_choice == 'E':
                    email = input("Enter the email you want to update: ")
                    found_user_data['email'] = email
                elif update_choice == 'A':
                    address = input("Enter the address you want to update: ")
                    found_user_data['address'] = address
                elif update_choice == 'P':
                    pincode = input("Enter the pincode you want to update: ")
                    found_user_data['is_valid_pincode'] = pincode
                elif update_choice == 'PN':
                    phone_number = input(
                        "Enter the phone number you want to update: ")
                    found_user_data['is_valid_phone_number'] = phone_number
                elif update_choice == 'Q':
                    updated_at = datetime.datetime.now()
                    found_user_data['updated_at'] = updated_at.strftime(
                        '%Y-%m-%d %H:%M:%S')

                    with open(self.data_file_path, 'w') as json_file:
                        json.dump(self.data, json_file, indent=4)

                    print("Updated successfully!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("user not found")

    def delete_user(self):
        account_number = input(
            'Enter Account Number of User You Want To Delete: ')
        found_user_data = None
        for user_data in self.data:
            if user_data['account_number'] == account_number:
                found_user_data = user_data
                break
        if found_user_data:
            confirm = input("Are you sure you want to delete? (Y/N): ").upper()

            if confirm == 'Y':
                found_user_data['is_active'] = False
                with open(self.data_file_path, 'w') as json_file:
                    json.dump(self.data, json_file, indent=4)
                print("Deleted Successfully!!")
            else:
                print("Data not deleted")
        else:
            print("user not found")

    def withdraw_amount(self):
        account_number = input("Enter your account number: ")
        withdrawal_amount = float(input("Enter the amount to withdraw: "))

        found_user_data = None
        for user_data in self.data:
            if user_data['account_number'] == account_number and user_data['is_active']:
                found_user_data = user_data
            if found_user_data:
                if withdrawal_amount <= found_user_data['total_amount']:
                    found_user_data['total_amount'] -= withdrawal_amount
                    transaction_history = TransactionHistory(account_number)
                    transaction_history.add_transaction(
                        "Withdrawal", withdrawal_amount)
                    if 'transaction_history' in found_user_data:
                        found_user_data['transaction_history'].extend(
                            transaction_history.transactions)
                    else:
                        found_user_data['transaction_history'] = transaction_history.transactions
                    with open(self.data_file_path, 'w') as json_file:
                        json.dump(self.data, json_file, indent=4)
                    print("Withdrawal successful, Total amount:",
                          found_user_data['total_amount'])
                else:
                    print("Insufficient balance!")
            else:
                print("User not found")

    def deposit_amount(self):
        account_number = input("Enter your account number: ")
        deposit_amount = float(input("Enter the amount to deposit: "))

        found_user_data = None
        for user_data in self.data:
            if user_data['account_number'] == account_number and user_data['is_active']:
                found_user_data = user_data
            if found_user_data:
                found_user_data['total_amount'] += deposit_amount
                transaction_history = TransactionHistory(account_number)
                transaction_history.add_transaction(
                    "Deposit", deposit_amount)
                if 'transaction_history' in found_user_data:
                    found_user_data['transaction_history'].extend(
                        transaction_history.transactions)
                else:
                    found_user_data['transaction_history'] = transaction_history.transactions
                with open(self.data_file_path, 'w') as json_file:
                    json.dump(self.data, json_file, indent=4)
                print("Deposit successful. Total amount:",
                      found_user_data['total_amount'])
            else:
                print("User not found!")

    def quit(self):
        print("You quit successfully")


if __name__ == "__main__":
    bank_system = MainBankSystem()
    bank_system.main()
