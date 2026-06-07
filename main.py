# ==================================
# E-Commerce Recommendation Engine
# Step 3: User Interaction System
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


class User:
    def __init__(self, user_id, name):

        self.user_id = user_id
        self.name = name

        # User interactions

        self.purchase_history = []
        self.search_history = []
        self.cart_items = []

        # Product ID -> Rating

        self.ratings = {}

    def display_profile(self):

        print("\n==============================")
        print("USER PROFILE")
        print("==============================")

        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")

        print("\nPurchase History:")
        print(self.purchase_history)

        print("\nSearch History:")
        print(self.search_history)

        print("\nCart Items:")
        print(self.cart_items)

        print("\nRatings:")
        print(self.ratings)


# ==================================
# Product Database (HashMap)
# ==================================

products = {}

products[101] = Product(101, "iPhone 15", "Electronics", 79999, 4.8)
products[102] = Product(102, "Samsung Galaxy S24", "Electronics", 74999, 4.7)
products[103] = Product(103, "Apple Watch", "Electronics", 39999, 4.6)
products[104] = Product(104, "Nike Running Shoes", "Fashion", 5999, 4.5)
products[105] = Product(105, "Adidas Hoodie", "Fashion", 2999, 4.4)
products[106] = Product(106, "Gaming Mouse", "Accessories", 1499, 4.7)
products[107] = Product(107, "Laptop Stand", "Accessories", 999, 4.3)
products[108] = Product(108, "Bluetooth Speaker", "Electronics", 2499, 4.5)
products[109] = Product(109, "Power Bank", "Accessories", 1299, 4.6)
products[110] = Product(110, "Jeans", "Fashion", 1999, 4.2)

# ==================================
# User Database (HashMap)
# ==================================

users = {}

# User 1

user1 = User(1001, "Anas")

user1.purchase_history = [
    101,
    103
]

user1.search_history = [
    "Electronics",
    "Accessories",
    "Laptop"
]

user1.cart_items = [
    109
]

user1.ratings = {
    101: 5,
    103: 5
}

users[user1.user_id] = user1

# User 2

user2 = User(1002, "Rahul")

user2.purchase_history = [
    104,
    105
]

user2.search_history = [
    "Fashion",
    "Shoes"
]

user2.cart_items = [
    110
]

user2.ratings = {
    104: 4,
    105: 5
}

users[user2.user_id] = user2


# ==================================
# Display Functions
# ==================================

def show_all_products():

    print("\n===== PRODUCT CATALOG =====\n")

    for product in products.values():
        product.display()


def show_all_users():

    show_recommendation_scores(user1)

    print("\n===== USER DATABASE =====")

    for user in users.values():
        user.display_profile()


# ==================================
# Main
# ==================================

def main():

    print("=" * 55)
    print(" E-Commerce Recommendation Engine")
    print(" Step 3: User Interaction System")
    print("=" * 55)

    show_all_products()

    show_all_users()
    
    
def calculate_recommendation_scores(user):

    scores = {}

    purchased_categories = set()
    cart_categories = set()
    searched_categories = set()

    # -------------------------
    # Purchase History Analysis
    # -------------------------

    for pid in user.purchase_history:
        purchased_categories.add(
            products[pid].category
        )

    # -------------------------
    # Cart Analysis
    # -------------------------

    for pid in user.cart_items:
        cart_categories.add(
            products[pid].category
        )

    # -------------------------
    # Search Analysis
    # -------------------------

    for item in user.search_history:
        searched_categories.add(item)

    # -------------------------
    # Score Every Product
    # -------------------------

    for pid, product in products.items():

        # Skip already purchased

        if pid in user.purchase_history:
            continue

        score = 0

        # Purchase category weight

        if product.category in purchased_categories:
            score += 5

        # Cart category weight

        if product.category in cart_categories:
            score += 4

        # Search category weight

        if product.category in searched_categories:
            score += 3

        # Rating weight

        score += product.rating

        scores[pid] = round(score, 2)

    return scores


def show_recommendation_scores(user):

    scores = calculate_recommendation_scores(user)

    print("\n===== RECOMMENDATION SCORES =====\n")

    for pid, score in scores.items():

        print(
            f"{products[pid].name:<25} Score = {score}"
        )


# ==================================
# Entry Point
# ==================================

if __name__ == "__main__":
    main()
    
    