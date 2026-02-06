# Function to check if a number is prime
def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check divisibility up to the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Function to perform basic calculator operations
def calculator(a, b, choice):
    if choice == "1":          # Addition
        return a + b

    elif choice == "2":        # Subtraction
        return a - b

    elif choice == "3":        # Multiplication
        return a * b

    elif choice == "4":        # Division
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid choice"


# ------------------ Main Program ------------------

# Prime Number Checker
num = int(input("Enter a number: "))

if is_prime(num):
    print("The number is prime")
else:
    print("The number is not prime")

print("-" * 30)

# Custom Calculator
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Choose an operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

op = input("Enter your choice (1/2/3/4): ")

result = calculator(x, y, op)
print("Result:", result)
