# Task 1: Build a Calculator CLI App - Elevate Labs

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {num1} {op} {num2} = {result}")

            choice = input("\nContinue? (yes/no): ").lower()
            if choice == 'no':
                print("Calculator Closed. Thank you!")
                break
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
