#Mini ATM System

balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Current Balance: ₹", balance)

elif choice == 2:
    amount = int(input("Enter Deposit Amount: "))
    balance += amount
    print("Updated Balance: ₹", balance)

elif choice == 3:
    amount = int(input("Enter Withdraw Amount: "))
    
    if amount <= balance:
        balance -= amount
        print("Updated Balance: ₹", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")