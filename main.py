secret_a = 15
secret_b = 87
secret_c = 7

guess = input("What is the number I am thinking?")

guess = input("Nop! Try again.")

if guess == "15":
    print("That is correct.")
elif guess == "87":
    print("You win!")
elif guess == "7":
    print("Hell yeah, you're right!.")
else:
    print("Nop! Try again.")