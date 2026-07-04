import random
secret_number = random.randint(1,100)
attempt = 0
print("welcome to random guess game")
print("im thinking of a number between 1 and 100.")
while True:
    guess = int(input("enter your guess:"))
    attempt += 1
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")
    else:
        print(f"correct you got it in{ attempt } attempt")
        break