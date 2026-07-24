# Assignment 5: Employee Attrition Prediction

## Objective
The objective of this assignment is to identify employees who are likely to leave the organization based on their demographic, professional, and work-related attributes. This is achieved by developing and comparing both Decision Tree and Random Forest classification models to predict employee attrition.

## Dataset Link
* [IBM HR Analytics Employee Attrition & Performance Dataset on Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)


## Libraries Used
* **Pandas**: For data loading, manipulation, and summary statistics.
* **NumPy**: For numerical computations and array operations.
* **Scikit-Learn (sklearn)**: For data preprocessing (encoding categorical variables), data splitting (`train_test_split`), building the models (`DecisionTreeClassifier`, `RandomForestClassifier`), and calculating evaluation metrics.
* **Matplotlib & Seaborn**: For data visualization, specifically generating Confusion Matrices and Feature Importance plots.

## Methodology
The project followed a structured machine learning pipeline:
1. **Data Understanding**: Loaded the dataset using Pandas, identified numerical and categorical features, and analyzed summary statistics.
2. **Data Preprocessing**: Checked for missing values, removed unnecessary columns with zero variance or identifiers, and applied one-hot encoding/label encoding for categorical variables. The dataset was then split into 80% training data and 20% testing data.
3. **Model Development**: Two classification models were trained on the training set: a Decision Tree Classifier and a Random Forest Classifier initialized with 100 estimators. Both models were used to predict employee attrition on the test dataset.
4. **Model Evaluation**: Both models were evaluated using Accuracy Score, Precision, Recall, and F1-Score. Visualizations were created to compare their Confusion Matrices and to plot the Feature Importances for the Random Forest model.

## Results

**Decision Tree Classifier:**
* **Accuracy Score**: 0.7585
* **Precision**: 0.1522
* **Recall**: 0.1795
* **F1-Score**: 0.1647

**Random Forest Classifier:**
* **Accuracy Score**: 0.8776
* **Precision**: 0.8000
* **Recall**: 0.1026
* **F1-Score**: 0.1818

## Model Comparison
1. The Random Forest model achieved a higher overall accuracy compared to the single Decision Tree model.
2. The Decision Tree exhibited higher variance, indicating that it likely captured noise in the training data, leading to a higher rate of false predictions on the test set.
3. Random Forest generally provides better precision, meaning when it predicts an employee will leave, it is more likely to be correct, though it may struggle to identify all at-risk employees (recall).
4. Feature importance analysis revealed that factors like Monthly Income, Age, and Total Working Years were the strongest predictors of attrition in the Random Forest model.

## Conclusion
In this assignment, we compared a Decision Tree Classifier with a Random Forest Classifier to predict employee attrition. Overall, the Random Forest model performed better, delivering higher accuracy and precision across the test dataset. 

Random Forest typically outperforms a single Decision Tree because it utilizes an ensemble learning method. By building multiple independent decision trees and aggregating their predictions, it effectively reduces the variance and overfitting that single trees are highly prone to. 

However, both models have limitations. A major limitation of Decision Trees is their extreme sensitivity to training data, making them prone to overfitting. Conversely, one limitation of Random Forests is their complexity and lack of interpretability; unlike a single decision tree which can be easily visualized, a random forest acts as a "black box," making it difficult to trace the exact logic of individual predictions.
