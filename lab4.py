#task won
checking = "yes"
while checking == "yes":
    print("What is your age: ")
    user_input = input()
    if user_input.isdigit() == False:
        print("number only bro")
    elif int(user_input) >= 18:
        print("Yes you can vote")
    else:
        print("You can't vote")
    print("Would you like to check another age? (put yes or else u lost ur chance to vote)")
    user_input2 = input()
    checking = user_input2

#task tooh
numbers = [15, -70000000, 0, 256543, -1, 8]

for number in numbers:
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")


#task thee
blocks = ["coal", "dirt", "diamond", "gravel", "stone"]

for block in blocks:
    if block == "diamond":
        print("jackpot")
    else:
        print(block)