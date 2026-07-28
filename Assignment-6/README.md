# Weather Condition Classification using SVM

## Objective
The objective of this project is to develop a Support Vector Machine (SVM) classification model to predict whether the weather is 'Cool' or 'Warm'. This classification is based on meteorological observations (Temperature, Relative Humidity, Surface Pressure, and Wind Speed) collected in real-time from the Open-Meteo API.

## API Documentation Link
* [Open-Meteo API Documentation](https://open-meteo.com/)

## Libraries Used
* **Python 3.x**
* `requests` - For fetching data from the Open-Meteo API.
* `pandas` - For data manipulation and DataFrame creation.
* `numpy` - For numerical operations and conditional logic.
* `scikit-learn` - For data preprocessing (`StandardScaler`, `LabelEncoder`), model development (`SVC`), and evaluation metrics.

## Methodology
1. **Data Collection:** Fetched 7 days of hourly weather data (temperature, relative humidity, surface pressure, and wind speed) for coordinates (Latitude: 28, Longitude: 77) via the Open-Meteo API.
2. **Data Preprocessing:** 
   * Converted JSON responses into a Pandas DataFrame.
   * Derived a target variable `Weather_Class` based on the rule: `Warm` if Temperature ≥ 25°C, otherwise `Cool`.
   * Removed non-predictive columns (e.g., time) and handled missing values.
   * Encoded the target categorical labels into numerical format.
   * Split the dataset into 80% training and 20% testing sets.
   * Standardized the input features using `StandardScaler` to ensure uniform scale.
3. **Model Development:** Trained a Support Vector Classifier (SVC) using the Radial Basis Function (RBF) kernel on the scaled training data.
4. **Model Evaluation:** Evaluated the model's predictive performance on the test set using Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.

## Results
The SVM model performed exceptionally well on the test dataset. By utilizing the RBF kernel and properly scaled features, the model achieved high accuracy, precision, and recall scores. The confusion matrix indicated a strong true positive and true negative rate, with very few misclassifications between the 'Warm' and 'Cool' categories.

## Conclusion
The Support Vector Machine (SVM) model successfully classified the weather conditions into 'Warm' and 'Cool' with high accuracy, demonstrating the effectiveness of the RBF kernel in handling meteorological data. A critical step in our methodology was feature scaling using `StandardScaler`. Because SVM is a distance-based algorithm, features with larger numerical ranges (like surface pressure) can disproportionately dominate the decision boundary over features with smaller ranges (like wind speed). Scaling ensures all features contribute equally to the model's predictions. 

One major advantage of the SVM algorithm is its robustness in modeling complex, non-linear relationships using the kernel trick (specifically the RBF kernel used here). However, a notable limitation is its potential computational inefficiency with very large datasets, as training time can scale quadratically or cubically with the number of observations, making it less suitable for massive real-time weather datasets.
