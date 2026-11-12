# Password-strength-checker-
A beginner Python tool that rates password strength and flags commonly used passwords.  
# Password Strength Checker

A command-line Python tool that checks how strong a password is and rates it
Weak, Medium, or Strong.

## Features
- Checks length (8+ characters)
- Detects uppercase letters, lowercase letters, digits, and symbols
- Gives a score out of 5
- Compares the password against a list of common passwords
- Always rates a common password as Weak, even if it passes every rule

## Why I built it
Attackers try common passwords first, so a password can follow every rule and
still be easy to guess. This project shows the difference between meeting
requirements and being secure.

## How to run
1. Install Python 3
2. Keep checker.py and common_passwords.txt in the same folder
3. Run: python checker.py

## Example
Enter your password: Hello123!
Length of password: 9
Has uppercase: True
Has lowercase: True
Has digits: True
Has symbols: True
Score: 5 / 5
Rating: Strong

## Concepts practiced
Loops, flag variables, conditionals, file handling, try/except, functions.

## Possible improvements
- Detect patterns such as aaaa1111 or qwerty
- Check several passwords in one run
- Estimate how long a brute-force attack would take
