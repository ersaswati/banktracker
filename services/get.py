import json

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
                        f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Timestamp: {transaction['timestamp']}")
        else:
            print("User not found")
