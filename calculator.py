def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Zero la divide panna mudiyaadhu!"
    return a / b


def main():
    while True:
        print("\n--- Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Choice select pannunga (1-5): ")

        if choice == "5":
            print("Bye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Thappana choice, thirumba try pannunga.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Number mattum enter pannunga!")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))


if __name__ == "__main__":
    main()