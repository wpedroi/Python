# Create inventory
inventory = {}

# Add items
for i in range(2):
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    inventory[item] = qty

# Selling process
choice = input("Do you want to sell? (y/n): ").lower()

if choice == 'y':
    item_name = input("Enter item name to sell: ")

    if item_name in inventory:
        print("Available quantity:", inventory[item_name])

        sell_qty = int(input("Enter quantity to sell: "))

        if sell_qty <= inventory[item_name]:
            inventory[item_name] -= sell_qty
            print("Sale successful.")
            print("Remaining quantity:", inventory[item_name])
        else:
            print("Error: Not enough quantity.")
    else:
        print("Error: Item not found.")

else:
    print("No selling operation.")

print("Final inventory:", inventory)