def generate_recommendations(df):
    recommendation_data = df.groupby("Product").agg({
        "Units_Sold": "mean",
        "Stock_Level": "min"
    }).reset_index()

    recommendations = []

    for _, row in recommendation_data.iterrows():
        average_daily_sales = row["Units_Sold"]
        current_stock = row["Stock_Level"]
        days_left = current_stock / average_daily_sales

        if days_left <= 5:
            status = "Reorder Immediately"
            priority = "HIGH"
            reorder_quantity = 250
        elif days_left <= 10:
            status = "Reorder Soon"
            priority = "MEDIUM"
            reorder_quantity = 150
        else:
            status = "Stock Level is Healthy"
            priority = "LOW"
            reorder_quantity = 0

        recommendations.append({
            "Product": row["Product"],
            "Current Stock": current_stock,
            "Average Daily Sales": round(average_daily_sales, 2),
            "Estimated Days Left": round(days_left, 1),
            "Recommendation": status,
            "Priority": priority,
            "Suggested Reorder Quantity": reorder_quantity
        })

    return recommendations