# -- coding: utf-8 --
"""
Created on Fri Apr 10 17:08:58 2026

@author: Student
Updated by: Andrei Montaniel (3ISC)
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


def simple_linear_regression(x, y):
    """Train and display simple linear regression details."""
    model = LinearRegression()
    model.fit(x, y)

    print("Simple Linear Regression Coefficients")
    print("Slope (Coefficient):", model.coef_[0])
    print("Intercept:", model.intercept_)
    print("-----------------------------")

    return model


def multiple_linear_regression(x, y):
    """Train and display multiple linear regression details."""
    model = LinearRegression()
    model.fit(x, y)

    print("Multiple Linear Regression Coefficients")
    print("Slope (Coefficient):", model.coef_)
    print("Intercept:", model.intercept_)
    print("-----------------------------")

    equation = (
        "Price = "
        f"({model.coef_[0]:.6f} * Size) + "
        f"({model.coef_[1]:.6f} * Bedrooms) + "
        f"({model.coef_[2]:.6f} * Age) + "
        f"({model.intercept_:.6f})"
    )
    print("Equation:", equation)

    return model


def get_house_input():
    """Prompt the user for house details and expected/actual price."""
    print("\nEnter house details for prediction:")
    size = float(input("Size (sq ft): "))
    bedrooms = int(input("Number of bedrooms: "))
    age = float(input("Age of the house (years): "))
    price = float(input("Price ($) [for comparison]: "))

    return size, bedrooms, age, price


def main():
    print("Activity #1: House Price Prediction")
    print("Student: Andrei Montaniel | Section: 3ISC")
    print("=" * 55)

    # Sample data from provided basis code (for simple and multiple demo)
    base_data = {
        "Feature1": [1, 3, 5, 7, 9],
        "Feature2": [1, 1, 2, 2, 3],
        "Target": [30, 40, 50, 60, 80],
    }
    base_df = pd.DataFrame(base_data)

    # Simple Linear Regression (Feature1 -> Target)
    simple_linear_regression(base_df[["Feature1"]], base_df["Target"])

    # Multiple Linear Regression (Feature1, Feature2 -> Target)
    multiple_linear_regression(base_df[["Feature1", "Feature2"]], base_df["Target"])

    print("\n--- Activity 1 Dataset (Real Estate) ---")
    # Activity #1 dataset
    data = {
        "Size": [1500, 1800, 2400, 3000, 3500],
        "Bedrooms": [3, 4, 3, 5, 4],
        "Age": [10, 15, 20, 8, 5],
        "Price": [250000, 320000, 350000, 420000, 490000],
    }
    df = pd.DataFrame(data)

    x = df[["Size", "Bedrooms", "Age"]]
    y = df["Price"]

    # Train model for activity requirements
    house_price_model = multiple_linear_regression(x, y)

    # Required prediction in the instructions
    required_house = pd.DataFrame({"Size": [2800], "Bedrooms": [4], "Age": [12]})
    required_prediction = house_price_model.predict(required_house)[0]

    print("\nRequired prediction:")
    print("House details: 2800 sq ft, 4 bedrooms, 12 years old")
    print(f"Predicted price: ${required_prediction:,.2f}")

    # User input prompt
    size, bedrooms, age, actual_price = get_house_input()
    user_house = pd.DataFrame(
        {
            "Size": [size],
            "Bedrooms": [bedrooms],
            "Age": [age],
        }
    )

    user_predicted_price = house_price_model.predict(user_house)[0]
    difference = actual_price - user_predicted_price

    print("\nYour house prediction result:")
    print(f"Input details: {size} sq ft, {bedrooms} bedrooms, {age} years old")
    print(f"Model predicted price: ${user_predicted_price:,.2f}")
    print(f"Inputted price: ${actual_price:,.2f}")
    print(f"Difference (Inputted - Predicted): ${difference:,.2f}")


if __name__ == "__main__":
    main()
