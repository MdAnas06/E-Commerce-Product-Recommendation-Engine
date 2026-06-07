# ==========================================================
# models.py
# E-Commerce Product Recommendation Engine
# ==========================================================



class Product:
    """
    Represents a product in the e-commerce catalog.
    """

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

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.category}) "
            f"₹{self.price} "
            f"Rating:{self.rating}"
        )


class User:
    """
    Represents a user and their interactions.
    """

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

    def __str__(self):
        return (
            f"User({self.user_id}, "
            f"{self.name})"
        )
        
        