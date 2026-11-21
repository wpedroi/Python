class Product:
    def __init__(self, pid, name, qty, price, profit):
        self.id = pid
        self.name = name
        self.qty = qty
        self.price = price
        self.profit = profit

    def total_value(self):
        return self.qty * self.price

    def total_profit(self):
        return self.qty * self.profit


class Sale:
    def __init__(self, product, qty):
        self.product_id = product.id
        self.product_name = product.name
        self.qty = qty
        self.price = product.price
        self.profit = product.profit * qty
        self.total = self._calculate_total(qty, product.price)

    @staticmethod
    def _calculate_total(qty, price):
        total = qty * price
        if qty >= 100:
            total *= 0.9   # 10% discount
        return total


class InventorySystem:
    def __init__(self):
        self.products = []
        self.sales = []

    # ---------- Product Management ----------
    def add_product(self):
        pid = int(input("Product ID: "))
        name = input("Name: ")
        qty = int(input("Quantity: "))
        price = int(input("Price per unit: "))
        profit = int(input("Profit per unit: "))
        self.products.append(Product(pid, name, qty, price, profit))
        print("Product added successfully.")

    def update_product(self):
        pid = int(input("Enter product ID to update: "))
        product = self._find_product(pid)
        if not product:
            print("Product not found.")
            return

        product.qty = int(input("New quantity: "))
        product.price = int(input("New price: "))
        product.profit = int(input("New profit per unit: "))
        print("Product updated successfully.")

    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        for i, p in enumerate(self.products, 1):
            print(f"""
Product {i}
ID: {p.id}
Name: {p.name}
Quantity: {p.qty}
Price per unit: {p.price}
Total value: {p.total_value()}
Profit per unit: {p.profit}
Total profit: {p.total_profit()}
Purchase price: {p.price - p.profit}
""")

    # ---------- Selling ----------
    def sell_product(self):
        pid = int(input("Enter product ID to sell: "))
        product = self._find_product(pid)

        if not product:
            print("Product not found.")
            return

        if product.qty <= 0:
            print("Product is out of stock.")
            return

        qty = int(input("Quantity to sell: "))
        if qty > product.qty:
            print("Not enough stock.")
            return

        product.qty -= qty
        sale = Sale(product, qty)
        self.sales.append(sale)

        print("Sold successfully.")
        print("Total price:", sale.total)
        print("Remaining quantity:", product.qty)

    # ---------- History ----------
    def selling_history(self):
        if not self.sales:
            print("No selling history.")
            return

        for i, s in enumerate(self.sales, 1):
            print(f"""
Sale {i}
Product ID: {s.product_id}
Name: {s.product_name}
Quantity sold: {s.qty}
Price per unit: {s.price}
Total price: {s.total}
Total profit: {s.profit}
""")

    # ---------- Helper ----------
    def _find_product(self, pid):
        for p in self.products:
            if p.id == pid:
                return p
        return None


# ================== MAIN PROGRAM ==================
system = InventorySystem()

while True:
    print("""
1- Add product
2- Update product
3- Display products
4- Sell product
5- Selling history
6- Exit
""")

    choice = input("Choose an option: ")

    if choice == '1':
        system.add_product()
    elif choice == '2':
        system.update_product()
    elif choice == '3':
        system.display_products()
    elif choice == '4':
        system.sell_product()
    elif choice == '5':
        system.selling_history()
    elif choice == '6':
        print("Exiting system...")
        break
    else:
        print("Invalid choice.")