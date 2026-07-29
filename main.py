def main():
    print("Welcome to the simple Python program!")
    print("This program can greet you and add two numbers.")

    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you.")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        total = a + b
        result = f"Hello, {name}! Nice to meet you.\nThe sum of {a} and {b} is {total}.\n"
        print(result.rstrip())
        with open("output.txt", "w", encoding="utf-8") as out_file:
            out_file.write(result)
        print("Output saved to output.txt")
    except ValueError:
        error_message = "Please enter valid numbers.\n"
        print(error_message.strip())
        with open("output.txt", "w", encoding="utf-8") as out_file:
            out_file.write(error_message)


if __name__ == "__main__":
    main()
