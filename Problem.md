                                                Problem Statement
Manually tracking bank account details (balances, transactions, account holder information) without a structured system is error-prone and does not scale beyond a handful of accounts.
This project addresses that by building a simple, structured banking system that can create accounts, safely handle deposits and withdrawals, and persist account data between sessions.
## Scope
The project implements a single-application, file-based banking system covering:
•	Account creation with basic government ID validation
•	Balance inquiries
•	Deposits and withdrawals with balance validation
•	Account detail lookup, gated by a captcha step
•	Basic account detail updates (name change)
The scope is intentionally limited to demonstrate core programming concepts (functions, data structures, file I/O, input validation, modular design) rather than to serve as a production-ready financial system. Security measures such as encryption and persistent PIN-based authentication are out of scope for this version (see README.md, "Limitations").
## Target Users
•	Students and instructors evaluating this project as a demonstration of programming fundamentals.
•	Hypothetically, an individual or small group wanting a simple local record of account balances without needing a real banking platform.
## High-Level Features
1.	Create Account — register a new account with a name and a government ID (ADHAAR or PANCARD), receiving a randomly generated account number.
2.	Check Balance — retrieve the current balance for any valid account number.
3.	Deposit / Withdraw — modify an account's balance, with validation to prevent withdrawing more than the available balance.
4.	Find Account — retrieve full account details, protected by a randomly generated captcha that must be re-entered correctly.
5.	Update — change the name associated with an account, after verifying the current name matches.
6.	Pin — set a transaction pin (currently verification-only; see README.md for the persistence limitation).

