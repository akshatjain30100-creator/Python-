class BankDatabase:
    def __init__(self, acc_no=0, acc_name="", acc_type="", op_bal=0.0):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.op_bal = op_bal
        self.total_bal = op_bal

    def showdata(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Name   : {self.acc_name}")
        print(f"Account Type   : {self.acc_type}")
        print(f"Opening Balance: {self.op_bal:.2f}")
        print(f"Total Balance  : {self.total_bal:.2f}")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to be withdrawn: "))
            if amount > self.total_bal:
                print("Insufficient balance.")
            else:
                self.total_bal -= amount
                print(f"Withdrawal successful. New Balance: {self.total_bal:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to be deposited: "))
            self.total_bal += amount
            print(f"Deposit successful. New Balance: {self.total_bal:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def exit_bank(self):
        print("\n----- Punjab National Bank -----")
        print("Thank you for using our services.")


def getdata():
    print("\n------------------- Welcome To ----------------")
    print("\n------------ Punjab National Bank -------------")
    print("\n------- Enter your following Credentials ------")
    acc_no = int(input("Enter the account number: "))
    acc_name = input("Enter the account name: ")
    acc_type = input("Enter the account type: ")
    op_bal = float(input("Enter the opening balance: "))
    return BankDatabase(acc_no, acc_name, acc_type, op_bal)


def main():
    s = getdata()
    while True:
        print("\n----- Punjab National Bank -----")
        print("1. Withdraw\n2. Deposit\n3. Show Account Details\n4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                s.withdraw()
            elif choice == 2:
                s.deposit()
            elif choice == 3:
                s.showdata()
            elif choice == 4:
                s.exit_bank()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
