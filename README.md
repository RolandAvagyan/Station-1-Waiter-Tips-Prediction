# Restaurant Tips Prediction

## Overview

This project focuses on predicting the amount of tips received in a restaurant setting based on various factors such as total bill amounts, customer demographics, and dining details. The dataset used contains information collected during restaurant transactions.

## Dataset

The dataset comprises the following columns:

- `total_bill`: Total amount of the bill.
- `tip`: Amount of tip received.
- `sex`: Gender of the customer.
- `smoker`: Whether the customer is a smoker or non-smoker.
- `day`: Day of the week when the transaction occurred.
- `time`: Time of the day for the dining experience (lunch or dinner).
- `size`: Size of the dining party.

## Analysis

1. **Data Exploration**: Utilized visualizations like scatter plots and pie charts to understand the relationships between various features and the tip amount.
   
2. **Data Preprocessing**: Employed one-hot encoding to handle categorical variables.
   
3. **Model Training**: Trained a Linear Regression model to predict tip amounts based on other features.
   
4. **Model Evaluation**: Evaluated the model using Mean Squared Error (MSE), a regression evaluation metric.

## Usage

1. **Requirements**: Ensure Python is installed along with required libraries (Pandas, NumPy, Plotly Express, Scikit-Learn).
   
2. **Dataset**: Download `data_set.csv` and place it in the script's directory.
   
3. **Execution**: Run the Python script (`analysis.py`).
   
4. **Interpretation**: Analyze visualizations and review evaluation metrics to understand model performance and relationships.

## Dependencies

- Python 3.10
- Pandas
- NumPy
- Plotly Express
- Scikit-Learn

## Results

The Linear Regression model achieved a Mean Squared Error (MSE) of 0.7 . Lower MSE indicates better model performance.

## Future Work

- Experiment with additional feature engineering techniques.
- Explore alternative regression algorithms for comparison.
- Gather more data to enhance the analysis and prediction capabilities.

