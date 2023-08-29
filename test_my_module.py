import unittest
from unittest.mock import patch
from services.insert import InsertModule
from services.get import GetModule
from services.update import UpdateModule
from services.delete import DeleteModule
from io import StringIO
import sys


class MyModuleTestCase(unittest.TestCase):
    def setUp(self):
        self.data_file_path = "data.json"

    @patch('builtins.input', side_effect=['John Doe', '1234567890', '12345', 'johndoe@example.com', '123 Main St', 'Sample Bank', 'SAMPLE123', 'Savings'])
    def test_create_account_2_valid_input(self, mock_input):
        interaction_log, user_input_details = InsertModule.create_account_gui(
            self.data_file_path)
        # Add assertions based on the expected values in interaction_log and user_input_details
        # For example:
        self.assertEqual(
            interaction_log["account_name"], "Enter your full name: ")
        self.assertEqual(user_input_details["account_name"], "John Doe")

    @patch('builtins.input', side_effect=[
        "John Doe",
        "123",          # invalid phone number
        "1234567890",   # valid phone number
        "12345", "john@example.com", "123 Main St", "My Bank", "ABC123", "Savings"])
    def test_create_account_2_invalid_phone(self, mock_input):

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as fake_stdout:
            InsertModule.create_account_gui(self.data_file_path)

        expected_error_message = "Phone number should be exactly 10 digits long and consist of digits only. Please re-enter."
        self.assertIn(expected_error_message, fake_stdout.getvalue())

    @patch('builtins.input', side_effect=[
        "John Doe", "1234567890",
        "123ABC",         # invalid pincode
        "123456",          # valid pincode
        "john@example.com", "123 Main St", "My Bank", "ABC123", "Savings"])
    def test_create_account_2_invalid_pincode(self, mock_input):

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as fake_stdout:
            InsertModule.create_account_gui(self.data_file_path)

        expected_error_message = "Pincode should consist of digits only. Please re-enter."
        self.assertIn(expected_error_message, fake_stdout.getvalue())

    @patch('builtins.input', side_effect=[
        "John Doe", "1234567890", "123456",
        "john example com"  # invalid email
        "john@example.com",  # valid email
        "123 Main St", "My Bank", "ABC123", "Savings"])
    def test_create_account_2_invalid_email(self, mock_input):

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as fake_stdout:
            InsertModule.create_account_gui(self.data_file_path)

        expected_error_message = "Invalid email address. Please enter a valid email."
        self.assertIn(expected_error_message, fake_stdout.getvalue())

    @patch('easygui.buttonbox', return_value="Account Number")
    @patch('builtins.input', side_effect=["1234567890"])
    def test_view_user_details_2_account_number(self, mock_buttonbox, mock_input):
        dummy1, dummy2, found_user_redux = GetModule.view_user_details_gui(
            self.data_file_path)
        expected = 'John Doe'
        self.assertEqual(found_user_redux, expected)

    @patch('easygui.buttonbox', return_value="Account Name")
    @patch('builtins.input', side_effect=["John Doe"])
    def test_view_user_details_2_account_name(self, mock_buttonbox, mock_input):
        dummy1, dummy2, found_user_redux = GetModule.view_user_details_gui(
            self.data_file_path)
        expected = 'John Doe'
        self.assertEqual(found_user_redux, expected)

    @patch('easygui.buttonbox', return_value="Phone Number")
    @patch('builtins.input', side_effect=["1234567890"])
    def test_view_user_details_2_phone_number(self, mock_buttonbox, mock_input):
        dummy1, dummy2, found_user_redux = GetModule.view_user_details_gui(
            self.data_file_path)
        expected = 'John Doe'
        self.assertEqual(found_user_redux, expected)

    @patch('builtins.input', side_effect=["1234567890", "400006"])
    @patch('easygui.buttonbox', side_effect=["Update User Details", "Pincode", "Quit", "Quit"])
    def test_update_user_details_2_update_details(self, mock_input, mock_buttonbox):
        interaction_log, user_input_details = UpdateModule.update_user_details_gui(
            self.data_file_path)
        self.assertEqual(
            interaction_log["new pincode"], "Enter the new pincode:")
        self.assertEqual(user_input_details["new pincode"], "400006")

    @patch('builtins.input', side_effect=["1234567890", "500"])
    @patch('easygui.buttonbox', side_effect=["Deposit Money", "Quit"])
    def test_update_user_details_2_deposit_money(self, mock_input, mock_buttonbox):
        interaction_log, user_input_details = UpdateModule.update_user_details_gui(
            self.data_file_path)
        self.assertEqual(
            interaction_log["deposit amount"], "Enter the amount to deposit:")
        self.assertEqual(user_input_details["deposit amount"], 500)

    @patch('builtins.input', side_effect=["1234567890", "100"])
    @patch('easygui.buttonbox', side_effect=["Withdraw Money", "Quit"])
    def test_update_user_details_2_withdraw_money(self, mock_input, mock_buttonbox):
        interaction_log, user_input_details = UpdateModule.update_user_details_gui(
            self.data_file_path)
        self.assertEqual(
            interaction_log["withdrawal amount"], "Enter the amount to withdraw:")
        self.assertEqual(user_input_details["withdrawal amount"], 100)

    @patch('builtins.input', side_effect=["1234567890"])
    @patch('easygui.buttonbox', return_value=["No"])
    def test_dete_user(self, mock_input, mock_buttonbox):
        interaction_log, user_input_details = DeleteModule.delete_user_gui(
            self.data_file_path)
        self.assertEqual(
            interaction_log["confirm"], "Are you sure you want to delete?")
        self.assertEqual(user_input_details["confirm"], ["No"])


if __name__ == '__main__':
    unittest.main()
