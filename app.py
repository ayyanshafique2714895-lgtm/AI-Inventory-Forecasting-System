import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.analytics import calculate_kpis
from src.recommendations import generate_recommendations
from src.forecast import generate_forecast
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

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.06);
}

[data-testid="stMetricLabel"] {
    font-size: 16px;
    font-weight: 600;
    color: #222222 !important;
}

[data-testid="stMetricValue"] {
    font-size: 34px;
    font-weight: 700;
    color: #111111 !important;
}
</style>
""", unsafe_allow_html=True)

# Read data
uploaded_file = st.sidebar.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

df = load_data(uploaded_file)

# Business Calculations
st.sidebar.header("Filters")

st.sidebar.subheader("📅 Date Filter")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Date"].max()
)

df = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

product_options = ["All Products"] + list(df["Product"].unique())

selected_product = st.sidebar.selectbox(
    "Select Product",
    product_options
)

search_product = st.sidebar.text_input(
    "🔍 Search Product"
)

if search_product:
    df = df[
        df["Product"].str.contains(
            search_product,
            case=False
        )
    ]

if selected_product != "All Products":
    df = df[df["Product"] == selected_product]

# Business Calculations
total_units, total_revenue, lowest_stock, best_product = calculate_kpis(df)

# Dashboard Title

st.sidebar.title("📦 Inventory AI")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "🤖 AI Forecast",
        "📦 Inventory Health",
        "📄 Reports"
    ]
)

st.sidebar.divider()
if page == "🏠 Dashboard":
    st.title("📦 AI Inventory Forecasting Dashboard")
    st.markdown(
        "AI-powered sales forecasting and inventory decision support for small businesses."
    )
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📦 Total Units Sold", total_units)
    col2.metric("💰 Revenue", f"${total_revenue}")
    col3.metric("⚠️ Lowest Stock", lowest_stock)
    col4.metric("🏆 Best Seller", best_product)

    st.divider()

        # Sales Data
    st.subheader("📊 Sales Data")
    st.dataframe(df)

    st.divider()
if page == "📊 Analytics":
    st.subheader("📈 Sales by Product")

    sales_by_product = get_sales_by_product(df).reset_index()

    fig = px.bar(
        sales_by_product,
        x="Product",
        y="Units_Sold",
        title="Sales by Product",
        text="Units_Sold"
    )

    fig.update_layout(
        template="plotly_white",
        title_font_size=20,
        xaxis_title="Product",
        yaxis_title="Units Sold"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("💰 Revenue by Product")

df["Revenue"] = df["Units_Sold"] * df["Price"]
revenue_by_product = get_revenue_by_product(df)

st.bar_chart(revenue_by_product)

st.subheader("📦 Stock Level by Product")

stock_by_product = get_stock_by_product(df)

st.bar_chart(stock_by_product)

st.divider()

st.subheader("📈 Sales Trend Over Time")

daily_sales = get_daily_sales(df)

st.line_chart(daily_sales)

st.divider()

st.subheader("🤖 AI Inventory Recommendations")

recommendations = generate_recommendations(df)

for rec in recommendations:
 st.write(f"### {rec['Product']}")
st.write(f"Current Stock: {rec['Current Stock']}")
st.write(f"Average Daily Sales: {rec['Average Daily Sales']}")
st.write(f"Estimated Days Left: {rec['Estimated Days Left']}")

if rec["Priority"] == "HIGH":
            st.error(f"🚨 Recommendation: {rec['Recommendation']}")
elif rec["Priority"] == "MEDIUM":
            st.warning(f"⚠️ Recommendation: {rec['Recommendation']}")
else:
            st.success(f"✅ Recommendation: {rec['Recommendation']}")

st.write(f"Suggested Reorder Quantity: **{rec['Suggested Reorder Quantity']} Units**")
st.write(f"Priority: **{rec['Priority']}**")

if page == "🤖 AI Forecast":
 st.subheader("🤖 7-Day AI Sales Forecast")

forecast_product = st.selectbox(
        "Select product for forecast",
        df["Product"].unique()
    )

forecast_df = generate_forecast(df, forecast_product, days=7)

st.dataframe(forecast_df)

st.line_chart(forecast_df.set_index("Day"))

st.divider()

st.subheader("📄 Download AI Forecast Report")

forecast_csv = forecast_df.to_csv(index=False)

st.download_button(
        label="⬇️ Download Forecast Report",
        data=forecast_csv,
        file_name="ai_forecast_report.csv",
        mime="text/csv"
    )

st.divider()

st.subheader("📄 Download Full Inventory Report")

report_df = df.copy()
report_df["Revenue"] = report_df["Units_Sold"] * report_df["Price"]

report_csv = report_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Full Inventory Report",
    data=report_csv,
    file_name="full_inventory_report.csv",
    mime="text/csv"
)