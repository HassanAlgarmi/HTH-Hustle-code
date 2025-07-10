# Step 1
def cat_greeting(word):
    print(f'Cat says {word}')
    print( 'Cat says nothing')
cat_greeting ("meow bruh")

# Step 2
def generate_superhero_power () :
    name = "gabe's"
    power = "super kindness"
    print(f"{name}'s power is {power}")
generate_superhero_power ()

# Step 3
def generate_superhero_power1():
    power = "flying"
    return power
print(generate_superhero_power1())


#step 4
def generate_superhero_power2(user_name, super_power):
    return f"{user_name}'s power is {super_power}"
(generate_superhero_power2("gabe", "super LYING"))

#step 5
def cat_greetings_loop():
    for _ in range(5):
        print("Meow bruh")
cat_greetings_loop()

#step 6
def generate_multiple_powers(powers):
    for power in powers:
        print(power)
generate_multiple_powers(["Flying", "Invisibility", "Super kindness"])