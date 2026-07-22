# AI-ML Assignment – 3: Salary Prediction using Polynomial Regression

## Objective
The objective of this assignment is to estimate the salary of employees based on their position level. Since the relationship between position level and salary is non-linear, a Polynomial Regression model is developed to accurately predict employee salaries.

## Dataset Link
[Position Salaries Dataset on Kaggle](https://www.kaggle.com/datasets/akram24/position-salaries)

## Libraries Used
* **Pandas:** For data loading, manipulation, and basic summary statistics.
* **NumPy:** For numerical operations and generating grid arrays for visualization.
* **Scikit-learn:** For data preprocessing (train-test split, polynomial features transformation) and model building (Linear Regression, evaluation metrics).
* **Matplotlib:** For data visualization, specifically plotting the original data points against the polynomial regression curve.

## Methodology
1. **Data Understanding:** Loaded the dataset using Pandas and identified the input feature (`Level`) and target variable (`Salary`).
2. **Data Preprocessing:** Checked for missing values and split the dataset into an 80% training set and a 20% testing set.
3. **Model Development:** Transformed the input features using Polynomial Features with a degree of 3, then trained a Linear Regression model on the transformed training data.
4. **Model Evaluation:** Evaluated the model's performance on the testing set using Mean Absolute Error (MAE), Mean Squared Error (MSE), and the $R^{2}$ Score. Visualized the final fit using a scatter plot overlaid with the polynomial regression curve.

## Results
The Polynomial Regression model successfully captured the non-linear relationship between position level and salary. The model's evaluation metrics (MAE, MSE, and $R^{2}$ Score) demonstrated a strong predictive capability on the test data. The visualization confirmed that the polynomial curve closely tracks the exponential increase in salaries at higher levels.

## Conclusion
Polynomial Regression proved to be highly effective for this dataset. By introducing polynomial terms, the model accommodated the steep increase in salaries at higher position levels, successfully avoiding the severe underestimation errors that would occur if a standard Linear Regression model were used.
