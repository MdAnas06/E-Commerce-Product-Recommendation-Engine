# ==========================================================
# main.py
# E-Commerce Product Recommendation Engine
# ==========================================================

from src.models import Product, User

from src.recommender import (
    display_recommendation_scores,
    display_ranked_recommendations,
    display_top_k_recommendations,
    display_similar_products,
    get_category_recommendations
)

from src.report_generator import (
    generate_report
)


# ==========================================================
# Product Database
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
# User Database
# ==========================================================

users = {}

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

def show_products():

    print("\n===== PRODUCT CATALOG =====\n")

    for product in products.values():
        product.display()


def show_users():

    print("\n===== USER DATABASE =====")

    for user in users.values():
        user.display_profile()


def show_category_recommendations():

    category = input(
        "\nEnter Category "
        "(Electronics/Fashion/Accessories): "
    )

    recommendations = get_category_recommendations(
        category,
        products
    )

    print(
        f"\n===== TOP PRODUCTS IN {category.upper()} =====\n"
    )

    if not recommendations:

        print("No products found.")
        return

    rank = 1

    for product in recommendations:

        print(
            f"{rank}. "
            f"{product.name:<25}"
            f" Rating: {product.rating}"
        )

        rank += 1


# ==========================================================
# CLI Menu
# ==========================================================

def menu():

    active_user = user1

    while True:

        print("\n" + "=" * 55)
        print(" E-Commerce Product Recommendation Engine")
        print("=" * 55)

        print("1. Show Product Catalog")
        print("2. Show Recommendation Scores")
        print("3. Show Ranked Recommendations")
        print("4. Show Top 5 Recommendations")
        print("5. Show Similar Products")
        print("6. Show Category Recommendations")
        print("7. Generate Recommendation Report")
        print("8. Show User Profiles")
        print("9. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            show_products()

        elif choice == "2":

            display_recommendation_scores(
                active_user,
                products
            )

        elif choice == "3":

            display_ranked_recommendations(
                active_user,
                products
            )

        elif choice == "4":

            display_top_k_recommendations(
                active_user,
                products,
                5
            )

        elif choice == "5":

            try:

                product_id = int(
                    input(
                        "\nEnter Product ID: "
                    )
                )

                if product_id not in products:

                    print("Invalid Product ID")
                    continue

                display_similar_products(
                    product_id,
                    products
                )

            except ValueError:

                print("Please enter a valid number.")

        elif choice == "6":

            show_category_recommendations()

        elif choice == "7":

            generate_report(
                active_user,
                products
            )

        elif choice == "8":

            show_users()

        elif choice == "9":

            print(
                "\nThank you for using the system."
            )

            break

        else:

            print(
                "\nInvalid choice. Try again."
            )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    menu()
    
    
    
