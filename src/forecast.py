import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def generate_forecast(df, product, days=7):
    forecast_data = df[df["Product"] == product].copy()
    forecast_data["Day"] = range(1, len(forecast_data) + 1)

    X = forecast_data[["Day"]]
    y = forecast_data["Units_Sold"]

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array(
        range(len(forecast_data) + 1, len(forecast_data) + days + 1)
    ).reshape(-1, 1)

    predictions = model.predict(future_days)

    forecast_df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, days + 1)],
        "Predicted Units Sold": predictions.round(2)
    })

    return forecast_df