# Expense Tracker - Part 2

expenses = []

while True:
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    expenses.append((name, amount))

    more = input("Add another? (y/n): ")
    if more.lower() != 'y':
        break

print("\nYour Expenses:")
for item in expenses:
    print(f"{item[0]} - ₹{item[1]}")

# Calculate total
total = sum([item[1] for item in expenses])
print(f"\nTotal Expenses: ₹{total}")
