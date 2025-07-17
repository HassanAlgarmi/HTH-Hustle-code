cookbook = []

def create(recipe):
     cookbook.append(recipe)
     print(f"here is the updated cookbook {cookbook}")

create(input("add a recipe" ))

def read(index):
    if 0 < index < len(cookbook):
        print(f"Recipe {cookbook[index]}")
    else:
        print("Index out of range. Cant read recipe.")

read(input("Enter the index of the recipe to read"))

def update(index, recipe):
    if 0 < index < len(cookbook):
        cookbook[index] = recipe
        print(f"Recipe at index {index} updated chnged to {recipe}.")
    else:
        print("Index out of range. Cant update recipe.")

update(input("Enter the index of the recipe to update")), (input("Enter the new recipe"))

def destroy(index):
    if 0 <  index < len(cookbook):
        removed_recipe = cookbook.pop(index)
        print(f"Recipe {removed_recipe} has been removed.")
    else:
        print("Index out of range. Cant delete recipe.")

destroy((input("Enter the index of the recipe you want to delete")))

def list_all_recipes():
    for i, in cookbook:
        print(cookbook[i])

list_all_recipes()




def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
1
