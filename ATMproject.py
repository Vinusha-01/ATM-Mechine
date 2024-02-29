

balance = 1000
scerete_pin = 5131

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    return f"Deposit successful. Your balance is now {balance}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient funds"
    else:
        balance -= amount
        return f"Withdrawal successful. Your balance is now {balance}"
    
    

while True:
  pin = int(input("enter your 4 digit pin: "))
  if pin != scerete_pin:
      print("invalid pin,please try again")      
  else:

    while True: 
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
         print("Your balance is:", check_balance())

        elif choice == 2:
          amount = float(input("Enter deposit amount: "))
          print(deposit(amount))

        elif choice == 3:
         amount = float(input("Enter withdrawal amount: "))
         print(withdraw(amount))

        elif choice == 4:
         print("Thank you for using the ATM. Goodbye!")
         break
        else:
           print("invalid option")

    break
  
