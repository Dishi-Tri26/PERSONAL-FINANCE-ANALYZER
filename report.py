def show_summary(data):
    print("\n--- Expense Summary ---")
    print(f"Number of expenses: {data['count']}")
    print(f"Total spending: Rs. {data['total']:.2f}")
    if data["highest"]:
        print("Highest category:", data["highest"])
    for category, amount in data["categories"].items():
        print(f"{category}: Rs. {amount:.2f}")
