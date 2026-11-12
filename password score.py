from main import password, has_lower, has_upper, has_symbol, has_digit

score = 0
if len(password) >= 8:
    score += 1
if has_lower:
    score += 1
if has_upper:
    score += 1
if has_symbol:
    score += 1
if has_digit:
    score += 1
print("score:", score)
if score <= 2:
    print("Rating: weak")
elif score <= 4:
    print("Rating: medium")
elif score <= 6:
    print("Rating: strong")
    def check_variety(password):
        has_digit = False
        has_symbol = False
        has_upper = False
        has_lower = False
        for char in password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True
            if char.lower():
                has_lower = True
            if char.symbol():
                has_symbol = True
                return has_digit, has_symbol, has_upper, has_lower