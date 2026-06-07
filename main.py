# ==================================
# E-Commerce Recommendation Engine
# Step 2: Product Dataset System
# ==================================

class Product:
    def __init__(self, product_id, name, category, price, rating):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating

    def display(self):
        print(
            f"ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Price: ₹{self.price} | "
            f"Rating: {self.rating}"
        )


# ==================================
# Product Database (HashMap)
# ==================================

products = {}

# ==================================
# Sample Product Catalog
# ==================================

products[101] = Product(
    101,
    "iPhone 15",
    "Electronics",
    79999,
    4.8
)

products[102] = Product(
    102,
    "Samsung Galaxy S24",
    "Electronics",
    74999,
    4.7
)

products[103] = Product(
    103,
    "Apple Watch",
    "Electronics",
    39999,
    4.6
)

products[104] = Product(
    104,
    "Nike Running Shoes",
    "Fashion",
    5999,
    4.5
)

products[105] = Product(
    105,
    "Adidas Hoodie",
    "Fashion",
    2999,
    4.4
)

products[106] = Product(
    106,
    "Gaming Mouse",
    "Accessories",
    1499,
    4.7
)

products[107] = Product(
    107,
    "Laptop Stand",
    "Accessories",
    999,
    4.3
)

products[108] = Product(
    108,
    "Bluetooth Speaker",
    "Electronics",
    2499,
    4.5
)

products[109] = Product(
    109,
    "Power Bank",
    "Accessories",
    1299,
    4.6
)

products[110] = Product(
    110,
    "Jeans",
    "Fashion",
    1999,
    4.2
)

# ==================================
# Display Functions
# ==================================

def show_all_products():
    print("\n===== PRODUCT CATALOG =====\n")

    for product in products.values():
        product.display()


def show_product_count():
    print(f"\nTotal Products Available: {len(products)}")


# ==================================
# Main Function
# ==================================

def main():
    print("=" * 50)
    print(" E-Commerce Product Recommendation Engine")
    print(" Step 2: Product Dataset System")
    print("=" * 50)

    show_product_count()
    show_all_products()


# ==================================
# Program Entry Point
# ==================================

if __name__ == "__main__":
    main()