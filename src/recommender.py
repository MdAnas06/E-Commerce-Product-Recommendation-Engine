# ==========================================================
# recommender.py
# Recommendation Engine Logic
# ==========================================================

import heapq


# ==========================================================
# Recommendation Scoring
# ==========================================================

def calculate_recommendation_scores(user, products):

    scores = {}

    purchased_categories = set()
    cart_categories = set()
    searched_categories = set()

    # Purchased categories

    for pid in user.purchase_history:
        if pid in products:
            purchased_categories.add(
                products[pid].category
            )

    # Cart categories

    for pid in user.cart_items:
        if pid in products:
            cart_categories.add(
                products[pid].category
            )

    # Search categories

    for item in user.search_history:
        searched_categories.add(item)

    # Score products

    for pid, product in products.items():

        # Skip purchased products

        if pid in user.purchase_history:
            continue

        score = 0

        # Purchase category match

        if product.category in purchased_categories:
            score += 5

        # Cart category match

        if product.category in cart_categories:
            score += 4

        # Search category match

        if product.category in searched_categories:
            score += 3

        # Product rating contribution

        score += product.rating

        scores[pid] = round(score, 2)

    return scores


# ==========================================================
# Ranking Recommendations
# ==========================================================

def rank_recommendations(user, products):

    scores = calculate_recommendation_scores(
        user,
        products
    )

    ranked_products = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_products


# ==========================================================
# Heap Top-K Recommendations
# ==========================================================

def get_top_k_recommendations(
        user,
        products,
        k=5):

    scores = calculate_recommendation_scores(
        user,
        products
    )

    heap = []

    for pid, score in scores.items():

        heapq.heappush(
            heap,
            (-score, pid)
        )

    recommendations = []

    for _ in range(min(k, len(heap))):

        score, pid = heapq.heappop(heap)

        recommendations.append(
            (pid, -score)
        )

    return recommendations


# ==========================================================
# Similar Product Recommendation
# ==========================================================

def get_similar_products(
        product_id,
        products,
        top_n=5):

    target_product = products[product_id]

    similar_products = []

    for pid, product in products.items():

        if pid == product_id:
            continue

        similarity_score = 0

        # Same category bonus

        if product.category == target_product.category:
            similarity_score += 10

        # Rating similarity

        rating_difference = abs(
            product.rating -
            target_product.rating
        )

        similarity_score += (
            5 - rating_difference
        )

        similar_products.append(
            (
                pid,
                round(similarity_score, 2)
            )
        )

    similar_products.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return similar_products[:top_n]


# ==========================================================
# Category Recommendations
# ==========================================================

def get_category_recommendations(
        category,
        products):

    category_products = []

    for product in products.values():

        if product.category.lower() == category.lower():

            category_products.append(product)

    category_products.sort(
        key=lambda product: product.rating,
        reverse=True
    )

    return category_products


# ==========================================================
# Utility Display Functions
# ==========================================================

def display_recommendation_scores(
        user,
        products):

    scores = calculate_recommendation_scores(
        user,
        products
    )

    print("\n===== RECOMMENDATION SCORES =====\n")

    for pid, score in scores.items():

        print(
            f"{products[pid].name:<25}"
            f" Score = {score}"
        )


def display_ranked_recommendations(
        user,
        products):

    ranked = rank_recommendations(
        user,
        products
    )

    print("\n===== RANKED RECOMMENDATIONS =====\n")

    rank = 1

    for pid, score in ranked:

        print(
            f"{rank}. "
            f"{products[pid].name:<25}"
            f" Score: {score}"
        )

        rank += 1


def display_top_k_recommendations(
        user,
        products,
        k=5):

    recommendations = get_top_k_recommendations(
        user,
        products,
        k
    )

    print(f"\n===== TOP {k} RECOMMENDATIONS =====\n")

    rank = 1

    for pid, score in recommendations:

        print(
            f"{rank}. "
            f"{products[pid].name:<25}"
            f" Score: {score}"
        )

        rank += 1



def display_similar_products(
        product_id,
        products):

    target = products[product_id]

    print(
        f"\n===== PRODUCTS SIMILAR TO: "
        f"{target.name} =====\n"
    )

    results = get_similar_products(
        product_id,
        products
    )

    rank = 1

    for pid, score in results:

        print(
            f"{rank}. "
            f"{products[pid].name:<25}"
            f" Similarity Score: {score}"
        )

        rank += 1