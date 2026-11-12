def main():
    password = input("Enter your password: ")

    try:
        with open("common_passwords.txt") as file:
            common = file.read().splitlines()
    except FileNotFoundError:
        print("Common password list not found, skipping that check.")
        common = []

    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    is_common = False          # NEW: flag, starts as "not found yet"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if password.lower() in common:   # NEW: moved up, runs before the rating
        is_common = True

    print("Length of password:", len(password))
    print("Has uppercase:", has_upper)
    print("Has lowercase:", has_lower)
    print("Has digits:", has_digit)
    print("Has symbols:", has_symbol)

    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    print("Score:", score, "/ 5")

    if is_common:                    # NEW: checked first
        print("Rating: Weak")
        print("Warning: this is a very common password!")
    elif score <= 2:
        print("Rating: Weak")
    elif score <= 4:
        print("Rating: Medium")
    else:
        print("Rating: Strong")


main()