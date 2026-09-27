from expense_manager import add_expense, show_expenses
from analyzer import analyze
from report import show_summary

def main():
    while True:
        print("\n--- Personal Finance and Expense Analysis ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show analysis")
        print("4. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_summary(analyze())
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
