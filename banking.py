login = "Gabat"
password = "gabat123"
attempt=3
while attempt > 0:
    user_login = input ("what is your login? ")
    user_password = input("what is your password?")
    if user_login == login and user_password == password:
        print("Welcome to Gabat")
        break
    else:
        attempt = attempt - 1
        print(f"you have{attempt} attempt left")

if attempt == 0:
    print("Account locked! too many attempt")

balance = 0
action = input("do you want to deposit, withdraw, or check balance")
if action == "deposit":
    amount: 100 = int(input("enter amount:"))
    balance = balance + amount
    print("new balance:", balance)

elif action == "withdraw":
    amount = int(input("enter amount:"))
    if balance > amount:
        balance = amount
        print("new balance:", balance)
    else:
        print("insufficient funds")

elif action == "check":
    print("your balance is:", balance)
    print("thank you for banking with us.")



