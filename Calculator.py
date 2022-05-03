import time
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("CalOS by:")
time.sleep(1)
print("Andromeda Industries 2022")
time.sleep(1)
print("Startup initiated")
time.sleep(3)
print("0_0")
time.sleep(1)
print("Hello World!")
time.sleep(3)
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:")
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("Result:")
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("Result:")
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Result:")
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Would you like to do another calculation? (yes/no): ")
        if next_calculation == "no":
            print("CalOS by:")
            time.sleep(1)
            print("Andromeda Industries 2022")
            time.sleep(1)
            print("Shutdown initiated")
            time.sleep(4)
            print("Shutdown complete! Killing program..")
            print("-_-")
            time.sleep(1)
            print("Goodbye world!")
            break
    
    else:
        print("Sorry, Invalid Input!")
