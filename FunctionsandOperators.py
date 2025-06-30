
menu = {'Pizza': 2.99,
        'Burger': 3.99,
        'Hot Dog': 1.99,
        'Cheese': 0.59,
        'Ice Cream': 1.49,
        'Churro': 0.79,
        'Soda': 0.89}

def total_price(*items):
    total = 0
    not_found = []
    
    for item in items:
        if item in menu:
            total += menu[item]
        else:
            not_found.append(item)
    
    if not_found:
        return f"The total price is ${total:.2f}. Missing items: {', '.join(not_found)}"
    else:
        return f"The total price is ${total:.2f}"

def price_difference(item1, item2):
    missing = []
    if item1 not in menu:
        missing.append(item1)
    if item2 not in menu:
        missing.append(item2)
    if missing:
        return f"Item(s) not found in menu: {', '.join(missing)}"
    
    price1 = menu[item1]
    price2 = menu[item2]
    difference = abs(price1 - price2)
    
    if price1 > price2:
        more_expensive = item1
        cheaper = item2
    elif price2 > price1:
        more_expensive = item2
        cheaper = item1
    else:
        return f"{item1} and {item2} cost the same: ${price1:.2f}"
    
    return f"The difference between {item1} and {item2} is ${difference:.2f}. {more_expensive} is more expensive than {cheaper}"

def inflation(item, multiplier):
    if item not in menu:
        return f"{item} not available. Cannot apply inflation"
    menu[item] = round(menu[item] * multiplier, 2)
    return menu

# Main execution
if __name__ == "__main__":
    # Test total_price function
    user_input = input("Enter menu items separated by commas: ")
    item_list = [item.strip() for item in user_input.split(',')]
    print(total_price(*item_list))
    
    # Test price_difference function
    item1 = input("Enter the first menu item you wish to compare: ").strip()
    item2 = input("Enter the second menu item you wish to compare: ").strip()
    print(price_difference(item1, item2))
    
    # Test inflation function
    item = input("Enter the menu item to inflate: ").strip()
    multiplier_input = input("Enter the multiplier for inflation: ").strip()
    try:
        multiplier = float(multiplier_input)
        updated_menu = inflation(item, multiplier)
        print("Updated menu:")
        print(updated_menu)
    except ValueError:
        print("Invalid multiplier. Please enter a number like 1.5")
