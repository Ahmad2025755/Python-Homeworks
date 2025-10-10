def is_disarium(number):
    num_str = str(number)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total == number

# Ask user to input a number
try:
    user_input = int(input("Enter a number: "))
    if is_disarium(user_input):
        print(f"{user_input} is a Disarium number.")
    else:
        print(f"{user_input} is not a Disarium number.")
except ValueError:
    print("Please enter a valid integer.")