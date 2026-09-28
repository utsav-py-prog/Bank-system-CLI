                                      Banking System cli
A command-line based banking system designed in Python, implemented as part of the Introduction to Programming and Problem solving course project.
## Introduction
The purpose of this project is to design and implement a simulation of some basic operations that one can perform in a bank account system like creating accounts, balance inquiry, deposit, withdrawal, updating accounts and searching accounts with a captcha verification facility. All the information related to accounts is stored locally in a text file (Account.txt).


## Features
•	Create Account – creates a new account using the ADHAAR ID (12 digits) or PANCARD ID (alphanumeric), and generates an auto-generated 10 digit account number.
•	Balance Inquiry – retrieves the current balance of the account.
•	Deposit – deposits money into the account.
•	Withdrawal – withdraws money from the account after checking the balance.
•	Update – changes the name of the account after validating the name.
•	Search Account – searches for all the details of the account (name, account number and balance) by a captcha security facility.
•	Pin – sets a transaction pin (See Limitations below).

## Tools/Technologies Used
Python 3
Only Built-In Modules: random, string
unittest for automatic testing
Storage in Text Files (No Database Needed)

## Installation and Execution Steps
1 Ensure Python 3 is installed on your computer.
2 Clone this repository and enter its project directory.
3 Run the program
4 Use the menu displayed to select a service. The accounts information will be stored in Account.txt which is located in the current directory. It will also be present during the next run of the program.

## Testing Instructions
Unit tests test account creation, deposits, withdrawals (including balance checking), and multiple account independence. 
Execute them using the following command:

python -m unittest tests/test_banking.py -v
Each test uses its own temporary file so that your actual Account.txt will never be touched.

## Non-Functional Requirements
Usability – menu driven interface with prompt and error message for bad inputs.
Reliability – account data saved across multiple runs in a file and malformed account entries are skipped and not causing the program to crash.
Maintainability – code is separated into modules performing specific functions (accounts, transactions, security, file storage) rather than being written in one script.
Error Handling – explicit checking of government ID number, lookup of account by number, and withdrawal when balance is not sufficient.
## Limitations/Future Enhancements
Pins are not persisted. Pin() function ensures two pins are identical, but it does not store the pin as part of an account record, thus it doesn't protect account from logins in the future. In the future implementation, pin field will be added to the account record format and checked in Find Account().
Not encrypted. Account records are stored in plaintext format, which is unacceptable for production.
Uses one file as a data storage rather than real database. This means that it cannot easily handle many accounts at once.
No logging of transaction for audit purposes.
