# ATM Simulator Project

balance = 10000
pin = "1234"

print("===== Welcome to Python ATM =====")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print(f"Your current balance is ₹{balance}")

        # Deposit Money
        elif choice == "2":
            deposit = float(input("Enter amount to deposit: ₹"))
            balance += deposit
            print(f"₹{deposit} deposited successfully.")
            print(f"Updated balance: ₹{balance}")

        # Withdraw Money
        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: ₹"))

            if withdraw <= balance:
                balance -= withdraw
                print(f"₹{withdraw} withdrawn successfully.")
                print(f"Remaining balance: ₹{balance}")
            else:
                print("Insufficient balance!")

        # Change PIN
        elif choice == "4":
            old_pin = input("Enter old PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new PIN: ")
                pin = new_pin
                print("PIN changed successfully!")
            else:
                print("Incorrect old PIN!")

        # Exit
        elif choice == "5":
            print("Thank you for using Python ATM.")
            break

        else:
            print("Invalid choice!")

else:
    print("Incorrect PIN! Access Denied.")