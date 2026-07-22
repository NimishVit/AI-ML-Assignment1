# Customer Churn Prediction using Logistic Regression

## Objective
To develop a Logistic Regression model to predict whether a telecommunications customer is likely to leave (churn) based on demographic information and service usage.

## Dataset Link
[Telco Customer Churn Dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Libraries Used
* **Pandas:** Data manipulation and analysis
* **NumPy:** Numerical computations
* **Scikit-learn:** Data preprocessing (`StandardScaler`, `train_test_split`), Model building (`LogisticRegression`), and Evaluation (`accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `confusion_matrix`)
* **Matplotlib & Seaborn:** Data visualization (Confusion Matrix heatmap)

## Methodology
1. **Data Understanding:** Loaded the dataset to identify numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`), categorical features, and the target variable (`Churn`).
2. **Data Preprocessing:** 
   * Handled missing values by coercing `TotalCharges` to numeric and dropping rows with missing data.
   * Dropped the irrelevant `customerID` column.
   * Encoded the target variable (`Churn`) into binary format (Yes=1, No=0).
   * Applied One-Hot Encoding to categorical features using `pd.get_dummies`.
   * Split the dataset into 80% training and 20% testing sets.
   * Scaled the features using `StandardScaler` to ensure optimal convergence for the Logistic Regression model.
3. **Model Development:** Initialized and trained a Logistic Regression model on the scaled training data.
4. **Model Evaluation:** Evaluated the model's predictions on the testing dataset using standard classification metrics and visualized the results using a confusion matrix.

## Results
* **Accuracy Score:** ~80%
* **Precision:** ~62%
* **Recall:** ~57%
* **F1-Score:** ~59%

**Observations:**
1. **Model Accuracy vs. Recall Trade-off:** While the model achieves a good overall accuracy, the recall for the churn class is comparatively lower. This means the model misses a noticeable portion of customers who actually churn (False Negatives).
2. **Precision Strength:** The precision score indicates that when the model predicts a customer will churn, it is generally correct about 65% of the time, preventing unnecessary retention spending on loyal customers.
3. **Class Imbalance Impact:** The confusion matrix reveals a higher number of True Negatives compared to True Positives. This reflects the natural class imbalance in the dataset, slightly biasing the model towards predicting "No Churn."

## Conclusion
The Logistic Regression model successfully predicted customer churn with roughly 80% accuracy, demonstrating that basic demographic and service usage data holds significant predictive power. Key findings indicate that customers with shorter tenures, month-to-month contracts, and higher monthly charges are at a significantly higher risk of leaving. Factors positively influencing retention include long-term contracts, tech support, and bundled services like online security. 

One primary limitation of Logistic Regression for this specific problem is its assumption of linear relationships between the log-odds of churn and the independent variables. It struggles to capture complex, non-linear interactions between features, which more advanced algorithms like Random Forest or Gradient Boosting could handle natively to improve recall rates for churners.
