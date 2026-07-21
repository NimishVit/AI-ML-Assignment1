# Medical Insurance Cost Prediction using Multiple Linear Regression

## Objective
The objective of this project is to develop a Multiple Linear Regression model to estimate the medical insurance charges of customers based on their personal and health-related information.

## Dataset Link
The project utilizes the **Medical Cost Personal Insurance Dataset** from Kaggle:
* [Kaggle Dataset URL](https://www.kaggle.com/datasets/mirichoi0218/insurance)

## Libraries Used
The following libraries were implemented to execute the analysis and build the predictive model:
* **Pandas**: Data loading, exploration, and structured profiling.
* **NumPy**: Linear algebra utilities and array operations.
* **Scikit-Learn (sklearn)**: Dataset division, model fitting, and baseline evaluation tracking.
* **Matplotlib**: Generation of performance diagnostics and evaluation charts.

---

## Methodology
1. **Data Understanding**: Loaded the raw dataset, inspected the initial records, and segmented the attributes into numerical features, categorical features, and the target variable (`charges`).
2. **Data Preprocessing**: Inspected the data frame for null entries, applied numerical structural encoding to categorical variables (`sex`, `smoker`, `region`), and split the final dataset into an 80% training segment and a 20% testing segment.
3. **Model Development**: Initialized a Multiple Linear Regression model utilizing all available personal and health features to predict the target variable.
4. **Model Evaluation**: Verified model predictive performance against the test dataset using distinct metric evaluations and scatter visualisations.

---

## Results & Model Evaluation (Task 4 Outline)

### Evaluation Metrics
* **Mean Absolute Error (MAE)**: `4181.19`
* **Mean Squared Error (MSE)**: `33596915.85`
* **R-squared ($R^2$) Score**: `0.78`

### Visualizations
* **Actual vs. Predicted Scatter Plot**: A generated scatter plot maps the actual test charges against the values predicted by the model, featuring a reference $y = x$ diagonal line to visually inspect error dispersion across different income brackets.
### Key Observations
1. **Impact of Specific Variables**: High-leverage features like smoking status and age cause distinct bands or strata to appear in the actual vs. predicted distribution, signifying major shifts in predicted risk.
2. **Variance Analysis**: The $R^2$ score demonstrates how much of the variance in customer billing behavior is successfully captured via linear feature trends.
3. **Underestimation at Higher Pricing Scales**: The model tends to struggle with outliers at the highest charge tiers, showing that plain linear paths may underpredict heavily compounded health risks.

---

## Conclusion (Task 5 Outline)

* **Key Findings**: The Multiple Linear Regression model serves as an effective baseline architecture for tracking and predicting customer healthcare expenditures based on core demographic and health data.
* **Factors Affecting Insurance Charges**: Evaluated model weights reveal that behavioral attributes—most notably smoking status—alongside systemic indicators like age and BMI stand out as the dominant variables driving higher insurance premiums.
* **Limitation of Linear Regression**: A key limitation of this model is its assumption of strict linearity between inputs and the target. It fails to implicitly capture non-linear synergies—such as the combined exponential threat seen when a high BMI explicitly interacts with smoking behaviors—without manually generating interaction or polynomial features.
