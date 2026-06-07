# ==========================================================
# report_generator.py
# Report Generation Module
# ==========================================================

from datetime import datetime

from src.recommender import (
    get_top_k_recommendations
)


def generate_report(
        user,
        products,
        output_file=
        "outputs/recommendation_report.txt"):

    recommendations = (
        get_top_k_recommendations(
            user,
            products,
            5
        )
    )

    with open(
            output_file,
            "w",
            encoding="utf-8") as file:

        file.write(
            "=====================================\n"
        )

        file.write(
            "E-COMMERCE RECOMMENDATION REPORT\n"
        )

        file.write(
            "=====================================\n\n"
        )

        file.write(
            f"Generated On: "
            f"{datetime.now()}\n\n"
        )

        file.write(
            f"User ID : {user.user_id}\n"
        )

        file.write(
            f"User Name : {user.name}\n\n"
        )

        file.write(
            "TOP RECOMMENDATIONS\n"
        )

        file.write(
            "----------------------------\n"
        )

        rank = 1

        for pid, score in recommendations:

            file.write(
                f"{rank}. "
                f"{products[pid].name} "
                f"(Score: {score})\n"
            )

            rank += 1

        file.write("\n")

        file.write(
            "PURCHASE HISTORY\n"
        )

        file.write(
            "----------------------------\n"
        )

        for pid in user.purchase_history:

            if pid in products:

                file.write(
                    f"{products[pid].name}\n"
                )

        file.write("\n")

        file.write(
            "SEARCH HISTORY\n"
        )

        file.write(
            "----------------------------\n"
        )

        for item in user.search_history:

            file.write(
                f"{item}\n"
            )

        file.write("\n")


        file.write(
            "CART ITEMS\n"
        )

        file.write(
            "----------------------------\n"
        )

        for pid in user.cart_items:

            if pid in products:

                file.write(
                    f"{products[pid].name}\n"
                )

    print(
        f"\nReport generated successfully:"
    )

    print(
        output_file
    )