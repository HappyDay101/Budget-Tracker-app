
import json

def main():
    print("Welcome to the Budget App!")
    initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter your expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again between # 1 to 3")

if __name__ == "__main__":
    main()
