import json
import datetime

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
                            email = input("Enter the email you want to update: ")
                            found_user_data['email'] = email
                        elif update_choice_2 == 'A':
                            address = input("Enter the address you want to update: ")
                            found_user_data['address'] = address
                        elif update_choice_2 == 'P':
                            pincode = input("Enter the pincode you want to update: ")
                            found_user_data['is_valid_pincode'] = pincode
                        elif update_choice_2 == 'PN':
                            phone_number = input(
                                "Enter the phone number you want to update: ")
                            found_user_data['is_valid_phone_number'] = phone_number
                        elif update_choice_2 == 'Q':
                            updated_at = datetime.datetime.now()
                            found_user_data['updated_at'] = updated_at.strftime('%Y-%m-%d %H:%M:%S')
                            with open(data_file_path, 'w') as json_file:
                                json.dump(data, json_file, indent=4)

                            break
                        else:
                            print("Invalid choice. Please try again.")
                
                elif update_choice == 'W':
                    withdrawal_amount = float(input("Enter the amount to withdraw: "))

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
                        updated_at = datetime.datetime.now()
                        found_user_data['updated_at'] = updated_at.strftime('%Y-%m-%d %H:%M:%S')
                        with open(data_file_path, 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        print("Withdrawal successful, Total amount:",
                            found_user_data['total_amount'])
                    else:
                        print("Insufficient balance!")
                
                elif update_choice == 'D':    
                    deposit_amount = float(input("Enter the amount to deposit: "))

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
                    found_user_data['updated_at'] = updated_at.strftime('%Y-%m-%d %H:%M:%S')
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
