import pandas as pd

data = {
    "Product_id": [],
    "name": [],
    "cur quantity": [],
    "pre qty": [],
    "price": [],
    "profit": []
}

static_data = {
    "pro_id": [],
    "name": [],
    "qyt_sold": [],
    "selling_percentage": [],
    "total_prof": []
}


def insert_pro():
    answer = 'y'
    print("\n\t\t ************************************<<insert Products>>************************************\n")
    while answer.lower() == 'y':
        data["Product_id"].append(input("Enter product ID: "))
        data["name"].append(input("Enter product name: "))
        data["cur quantity"].append(int(input("Enter product quantity: ")))
        data["pre qty"] = data["cur quantity"].copy()
        data["price"].append(int(input("Enter product price: ")))
        data["profit"].append(int(input("Enter product profit: ")))
        answer = input("Do you want to add more products (Enter Y as Yes & N as No): ")


def sell_pro():
    # if data.__sizeof__()
    print("\n\t\t ************************************<<Sell Products>>************************************\n")
    df = pd.DataFrame(data)
    print(df)
    answer = 'y'
    while answer.lower() == 'y':
        pro_index = int(input("What do you want to sell Enter Index: "))
        print("Element is ", data["name"][pro_index], str(data["quantity"][pro_index]))
        qty = int(input("Enter Quantity: "))
        while qty > data["quantity"][pro_index]:
            print("Quantity is not enough!")
            qty = int(input("Enter Quantity again: "))
        print("Element Sold..........")
        if data["Product_id"][pro_index] in static_data["pro_id"]:
            static_data["qyt_sold"][pro_index] += qty
            static_data["selling_percentage"][pro_index] = ((static_data["qyt_sold"][pro_index] / first_qty) * 100)
            static_data["total_prof"][pro_index] += qty * data["profit"][pro_index]
        else:
            static_data["pro_id"].append(data["Product_id"][pro_index])
            static_data["name"].append(data["name"][pro_index])
            static_data["qyt_sold"].append(qty)
            static_data["selling_percentage"].append(((qty / data["quantity"][pro_index]) * 100))
            static_data["total_prof"].append(qty * data["profit"][pro_index])
            first_qty = data["quantity"][pro_index]
        data["quantity"][pro_index] -= qty
        print(pd.DataFrame(data))
        answer = input("Do you want to Sell more products (Enter Y as Yes & N as No): ")


def show_pro():
    print("\n\t\t ************************************<<Show Products>>************************************\n")
    df = pd.DataFrame(data)
    print("\n", df, "\n")


def selling_statistics():
    print("\n\t\t ************************************<<Selling Statistics>>************************************\n")
    static_df = pd.DataFrame(static_data)
    print("\n", static_df, "\n")
    n = 0
    for i in static_df["selling_percentage"]:
        if i >= 90:
            print("Product ", static_df["name"][n], " is about to run out!")
        elif i == 100:
            print("Warning! Product ", static_df["name"][n], " has run out!")
    n += 1


x = 1

while x != 5:
    print("\t\t\t\t\t~~~~~~~~~~~~~<<< WELCOME >>>~~~~~~~~~~~~~\n\n..........................|"
          "MENU|..........................")

    x = int(input("print \n(1) to Add products\n(2) to sell products\n(3) to view all products\n(4) to see "
                  "statistics\n(5) to Exit\nWhat do you want to do\nEnter a Number: "))

    if x == 1:
        insert_pro()
    elif x == 2:
        sell_pro()
    elif x == 3:
        show_pro()
    elif x == 4:
        selling_statistics()
    elif x == 5:
        print("Exiting........")
    else:
        print("Not Found!")


df = pd.read_json(r"countries of the world.json")
df