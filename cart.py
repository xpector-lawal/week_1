# Default stored user database
user_database = {
    "Elijah": "1234",
    "Lawal": "0000",
    "Glory": "1345"
}


# Available product database
products_database = {
    1: {"name": "Laptop", "price": 500000},
    2: {"name": "Smartphone", "price": 250000},
    3: {"name": "Headphones", "price": 30000},
    4: {"name": "Keyboard", "price": 15000}
}


# Shopping cart
shopping_cart = []


# Login function
def user_login():
    print("===== LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in user_database and user_database[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid login credentials.")
        return False


# Function to display available products
def view_products():
    print("\n===== AVAILABLE PRODUCTS =====")

    for product_id, product in products_database.items():
        print(
            f"{product_id}. {product['name']} - "
            f"₦{product['price']:,}"
        )


# Function to add product to cart
def add_to_cart():
    view_products()

    try:
        product_id = int(
            input("\nEnter product number to add to cart: ")
        )

        if product_id in products_database:
            shopping_cart.append(products_database[product_id])

            print(
                f"{products_database[product_id]['name']} "
                "added to cart."
            )
        else:
            print("Product not found.")

    except ValueError:
        print("Please enter a valid product number.")


# Function to view cart
def view_cart():
    print("\n===== YOUR CART =====")

    if len(shopping_cart) == 0:
        print("Your cart is empty.")
        return

    total = 0

    for item in shopping_cart:
        print(f"- {item['name']} - ₦{item['price']:,}")
        total += item["price"]

    print("----------------------")
    print(f"Total: ₦{total:,}")


# Main program
if user_login():

    while True:
        print("\n===== E-COMMERCE MENU =====")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            view_cart()

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid option. Please try again.")