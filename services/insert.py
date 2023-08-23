import random
import datetime
import json
import re
import os


class InsertModule:
    @staticmethod
    def is_valid_phone_number(phone_number):
        return len(str(phone_number)) == 10 and str(phone_number).isdigit()

    @staticmethod
    def is_valid_pincode(pincode):
        return str(pincode).isdigit()

    @staticmethod
    def create_account(data_file_path):
        name = input("Enter your full name: ")
        account_number = str(random.randint(1000000000, 9999999999))
        print("Your Account Number:", account_number)
        while True:
            phone_number = input("Enter your phone number: ")
            if InsertModule.is_valid_phone_number(phone_number):
                break
            print(
                "Phone number should be exactly 10 digits long and consist of digits only. Please re-enter.")
        while True:
            pincode = input("Enter your pincode: ")
            if InsertModule.is_valid_pincode(pincode):
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

        user_data = {
            "account_name": name,
            "account_number": account_number,
            "is_valid_phone_number": phone_number,
            "is_valid_pincode": pincode,
            "email": email,
            "address": address,
            "bank_name": bank_name,
            "ifsc": ifsc,
            "account_type": account_type,
            "total_amount": total_amount,
            "is_active": True,
            "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": None
        }

        if os.path.exists(data_file_path):
            with open(data_file_path) as json_file:
                data = json.load(json_file)
        else:
            data = []

        data.append(user_data)

        with open(data_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("User added successfully!")

    def create_account_2(data_file_path):
        name = input("Enter your full name: ")
        account_number = str(random.randint(1000000000, 9999999999))
        print("Your Account Number:", account_number)
        while True:
            phone_number = input("Enter your phone number: ")
            if InsertModule.is_valid_phone_number(phone_number):
                break
            print(
                "Phone number should be exactly 10 digits long and consist of digits only. Please re-enter.")
        while True:
            pincode = input("Enter your pincode: ")
            if InsertModule.is_valid_pincode(pincode):
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

        user_data = {
            "account_name": name,
            "account_number": account_number,
            "phone_number": phone_number,
            "pincode": pincode,
            "email": email,
            "address": address,
            "bank_name": bank_name,
            "ifsc": ifsc,
            "account_type": account_type,
            "total_amount": total_amount,
            "is_active": True,
            "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": None
        }

        if os.path.exists(data_file_path):
            with open(data_file_path) as json_file:
                data = json.load(json_file)
        else:
            data = []

        data.append(user_data)

        with open(data_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("User added successfully!")

        interaction_log = {
            "account_name": "Enter your full name: ",
            "phone_number": "Enter your phone number: ",
            "pincode": "Enter your pincode: ",
            "email": "Enter your e-mail ID: ",
            "address": "Enter your address: ",
            "bank_name": "Enter your bank_name: ",
            "ifsc": "Enter your IFSC code: ",
            "account_type": "Enter your account_type: "
        }

        user_input_details = {
            "account_name": name,
            "phone_number": phone_number,
            "pincode": pincode,
            "email": email,
            "address": address,
            "bank_name": bank_name,
            "ifsc": ifsc,
            "account_type": account_type
        }

        return interaction_log, user_input_details
