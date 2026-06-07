# ==========================================================
# E-Commerce Product Recommendation Engine
# Step 6: Heap-Based Top-K Recommendation System
# ==========================================================

import heapq


# ==========================================================
# Product Class
# ==========================================================

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


# ==========================================================
# User Class
# ==========================================================

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        self.purchase_history = []
        self.search_history = []
        self.cart_items = []
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


# ==========================================================
# Product Database (HashMap)
# ==========================================================

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


# ==========================================================
# User Database (HashMap)
# ==========================================================

users = {}

# User 1

user1 = User(1001, "Anas")

user1.purchase_history = [101, 103]

user1.search_history = [
    "Electronics",
    "Accessories",
    "Laptop"
]

user1.cart_items = [109]

user1.ratings = {
    101: 5,
    103: 5
}

users[user1.user_id] = user1

# User 2

user2 = User(1002, "Rahul")

user2.purchase_history = [104, 105]

user2.search_history = [
    "Fashion",
    "Shoes"
]

user2.cart_items = [110]

user2.ratings = {
    104: 4,
    105: 5
}

users[user2.user_id] = user2


# ==========================================================
# Display Functions
# ==========================================================

def show_all_products():
    print("\n===== PRODUCT CATALOG =====\n")

    for product in products.values():
        product.display()


def show_all_users():
    print("\n===== USER DATABASE =====")

    for user in users.values():
        user.display_profile()


# ==========================================================
# Recommendation Scoring Engine
# ==========================================================

def calculate_recommendation_scores(user):

    scores = {}

    purchased_categories = set()
    cart_categories = set()
    searched_categories = set()

    # Purchase history categories

    for pid in user.purchase_history:
        purchased_categories.add(
            products[pid].category
        )

    # Cart categories

    for pid in user.cart_items:
        cart_categories.add(
            products[pid].category
        )

    # Search categories

    for item in user.search_history:
        searched_categories.add(item)

    # Calculate score for every product

    for pid, product in products.items():

        # Exclude already purchased products

        if pid in user.purchase_history:
            continue

        score = 0

        # Purchase match

        if product.category in purchased_categories:
            score += 5

        # Cart match

        if product.category in cart_categories:
            score += 4

        # Search match

        if product.category in searched_categories:
            score += 3

        # Product rating

        score += product.rating

        scores[pid] = round(score, 2)

    return scores


# ==========================================================
# Display Scores
# ==========================================================

def show_recommendation_scores(user):

    scores = calculate_recommendation_scores(user)

    print("\n===== RECOMMENDATION SCORES =====\n")

    for pid, score in scores.items():

        print(
            f"{products[pid].name:<25} Score = {score}"
        )


# ==========================================================
# Sorting-Based Ranking
# ==========================================================

def rank_recommendations(user):

    scores = calculate_recommendation_scores(user)

    ranked_products = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_products


def show_ranked_recommendations(user):

    ranked = rank_recommendations(user)

    print("\n===== RANKED RECOMMENDATIONS =====\n")

    rank = 1

    for pid, score in ranked:

        print(
            f"{rank}. "
            f"{products[pid].name:<25}"
            f" Score: {score}"
        )

        rank += 1


# ==========================================================
# Heap-Based Top-K Recommendation Engine
# ==========================================================

def get_top_k_recommendations(user, k=5):

    scores = calculate_recommendation_scores(user)

    heap = []

    for pid, score in scores.items():

        heapq.heappush(
            heap,
            (-score, pid)
        )

    top_products = []

    for _ in range(min(k, len(heap))):

        score, pid = heapq.heappop(heap)

        top_products.append(
            (pid, -score)
        )

    return top_products


def show_top_k_recommendations(user, k=5):

    recommendations = get_top_k_recommendations(user, k)

    print(f"\n===== TOP {k} RECOMMENDATIONS (HEAP) =====\n")

    rank = 1

    for pid, score in recommendations:

        print(
            f"{rank}. "
            f"{products[pid].name:<25}"
            f" Score: {score}"
        )

        rank += 1


# ==========================================================
# Main Function
# ==========================================================

def main():

    print("=" * 60)
    print(" E-Commerce Product Recommendation Engine")
    print(" Step 6: Heap-Based Top-K Recommendations")
    print("=" * 60)

    # Product Data

    show_all_products()

    # Recommendation Scores

    show_recommendation_scores(user1)

    # Sorted Ranking

    show_ranked_recommendations(user1)

    # Heap-Based Top K

    show_top_k_recommendations(user1, 5)

    # User Data

    show_all_users()


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()
    
    
    