import streamlit as st
import pandas as pd

from src.recommendations import generate_recommendations
from src.forecast import generate_forecast
from src.data_loader import load_data
from src.analytics import calculate_kpis
from src.visualizations import (
    get_sales_by_product,
    get_revenue_by_product,
    get_stock_by_product,
    get_daily_sales
)

st.set_page_config(
    page_title="AI Inventory Forecasting System",
    page_icon="📦",
    layout="wide"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

df = load_data(uploaded_file)

total_units, total_revenue, lowest_stock, best_product = calculate_kpis(df)

st.sidebar.title("📦 Inventory AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "🤖 AI Forecast",
        "📦 Inventory Health",
        "📄 Reports"
    ]
)

if page == "🏠 Dashboard":
    st.title("📦 AI Inventory Forecasting Dashboard")
    st.markdown("AI-powered sales forecasting and inventory decision support for small businesses.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
     st.metric("📦 Total Units Sold", f"{total_units:,}")

    with col2:
     st.metric("💰 Revenue", f"${total_revenue:,.0f}")

    with col3:
     st.metric("⚠️ Lowest Stock", lowest_stock)

    with col4:
     st.metric("🏆 Best Seller", best_product)

    st.divider()

    st.subheader("📊 Sales Data")
    st.dataframe(df)

elif page == "📊 Analytics":
    st.title("📊 Analytics")

    st.subheader("📈 Sales by Product")
    sales_by_product = get_sales_by_product(df)
    st.bar_chart(sales_by_product)

    st.divider()

    st.subheader("💰 Revenue by Product")
    df["Revenue"] = df["Units_Sold"] * df["Price"]
    revenue_by_product = get_revenue_by_product(df)
    st.bar_chart(revenue_by_product)

    st.divider()

    st.subheader("📦 Stock Level by Product")
    stock_by_product = get_stock_by_product(df)
    st.bar_chart(stock_by_product)

    st.divider()

    st.subheader("📉 Sales Trend")
    daily_sales = get_daily_sales(df)
    st.line_chart(daily_sales)
   # Sales by Product chart

    st.divider()

    st.subheader("💰 Revenue by Product")
    # Revenue chart

    st.divider()

    st.subheader("📦 Stock Level by Product")
    # Stock chart

    st.divider()

    st.subheader("📉 Sales Trend")
    # Trend chart

elif page == "🤖 AI Forecast":
    st.title("🤖 7-Day AI Sales Forecast")

    forecast_product = st.selectbox(
        "Select product for forecast",
        df["Product"].unique()
    )

    forecast_df = generate_forecast(df, forecast_product, days=7)

    st.dataframe(forecast_df)

    st.line_chart(
        forecast_df,
        x="Day",
        y="Predicted Units Sold"
    )
elif page == "📦 Inventory Health":
    st.title("📦 Inventory Health")

    recommendations = generate_recommendations(df)

    for rec in recommendations:
        st.subheader(rec["Product"])

        st.write(f"Current Stock: **{rec['Current Stock']}**")
        st.write(f"Average Daily Sales: **{rec['Average Daily Sales']}**")
        st.write(f"Estimated Days Left: **{rec['Estimated Days Left']} days**")
        st.write(f"Suggested Reorder Quantity: **{rec['Suggested Reorder Quantity']} Units**")

        if rec["Priority"] == "HIGH":
            st.error(f"🚨 {rec['Recommendation']} | Priority: HIGH")
        elif rec["Priority"] == "MEDIUM":
            st.warning(f"⚠️ {rec['Recommendation']} | Priority: MEDIUM")
        else:
            st.success(f"✅ {rec['Recommendation']} | Priority: LOW")

        st.divider()
elif page == "📄 Reports":
    st.title("📄 Reports")

    df["Revenue"] = df["Units_Sold"] * df["Price"]

    inventory_csv = df.to_csv(index=False)

    st.subheader("📄 Download Full Inventory Report")
    st.download_button(
        label="⬇️ Download Full Inventory Report",
        data=inventory_csv,
        file_name="full_inventory_report.csv",
        mime="text/csv"
    )

    st.divider()

    forecast_product = st.selectbox(
        "Select product for forecast report",
        df["Product"].unique()
    )

    forecast_df = generate_forecast(df, forecast_product, days=7)
    forecast_csv = forecast_df.to_csv(index=False)

    st.subheader("📄 Download AI Forecast Report")
    st.download_button(
        label="⬇️ Download Forecast Report",
        data=forecast_csv,
        file_name="ai_forecast_report.csv",
        mime="text/csv"
    )