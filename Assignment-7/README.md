# Customer Segmentation using K-Means Clustering and PCA

## Objective
The objective of this project is to develop a K-Means Clustering model to divide mall customers into distinct groups based on their annual income and spending behavior. These segments will be used by management for targeted marketing campaigns. Additionally, Principal Component Analysis (PCA) is applied to visualize the high-dimensional customer clusters in two dimensions.

## Dataset Link
* [Mall Customer Segmentation Dataset (Kaggle)](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

## Libraries Used
* **Pandas:** For loading the dataset, data manipulation, and summary statistics.
* **Scikit-learn:** For data preprocessing (`StandardScaler`, `LabelEncoder`), model development (`KMeans`), and dimensionality reduction (`PCA`).
* **Matplotlib & Seaborn:** For generating the Elbow Curve and plotting the customer clusters and PCA scatter plots.

## Methodology
1. **Data Understanding & Preprocessing:** Loaded the dataset and identified numerical and categorical features. Unnecessary columns (like CustomerID) were removed, categorical variables were encoded, and numerical features were standardized using `StandardScaler`.
2. **Model Development:** The Elbow Method was utilized to determine the optimal number of clusters (K). A K-Means model was then trained to assign cluster labels to each customer.
3. **Dimensionality Reduction:** Applied PCA to reduce the scaled dataset into 2 principal components for visualization purposes.
4. **Visualization:** Generated scatter plots to display the clusters based on original features and the PCA-reduced dimensions.

## Results
The Elbow Method indicated an optimal cluster count of $k=5$. The K-Means model successfully segmented the customers into five distinct groups representing different combinations of income and spending behaviors. The PCA transformation effectively condensed the variance into two components, allowing for clear 2D visualization of the identified customer groups. 

## Conclusion
The K-Means clustering algorithm successfully segmented the mall customers into five distinct groups based on their annual income and spending behavior. These key findings reveal clear behavioral patterns, such as high-income/high-spending and low-income/low-spending groups. From a business perspective, these customer segments are highly valuable for targeted marketing campaigns. For instance, management can deploy exclusive loyalty programs for the most profitable group or offer specific discounts to budget-conscious shoppers. 

While K-Means is highly efficient, one notable limitation is that it requires the optimal number of clusters (K) to be manually defined beforehand and can be sensitive to outliers. Conversely, applying Principal Component Analysis (PCA) provided a significant advantage by reducing the computational complexity and dimensionality of the dataset. This allowed us to effectively visualize the complex customer clusters on a 2D plane while preserving the most critical patterns in the data.
