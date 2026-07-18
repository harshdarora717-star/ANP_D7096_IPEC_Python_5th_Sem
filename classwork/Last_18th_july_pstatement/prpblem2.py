#Problem 2: Bank Account System 
class BankAccount:

    def accept_details(self):
        self.account_number = input("Enter Account Number : ")
        self.customer_name = input("Enter Customer Name : ")
        self.balance = float(input("Enter Initial Balance : "))

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Current Balance :", self.balance)


# Create an object of BankAccount class
account1 = BankAccount()

# Accept account details
account1.accept_details()

# Accept deposit amount
deposit_amount = float(input("Enter Deposit Amount : "))
account1.deposit(deposit_amount)

# Accept withdrawal amount
withdraw_amount = float(input("Enter Withdrawal Amount : "))
account1.withdraw(withdraw_amount)

# Display final account details and balance
account1.display_balance()




#output:
'''
------ Bank Account Details ------
Account Number : 101
Account Holder : anjali
Balance        : 24000.0             
Enter Account Number : 23456444565456
Enter Customer Name : anjali
Enter Initial Balance : 98000
Enter Deposit Amount : 98000
Amount Deposited Successfully.
Enter Withdrawal Amount : 000
Amount Withdrawn Successfully.

------ Account Details ------
Account Number : 23456444565456
Customer Name  : anjali
Current Balance : 196000.0
'''