# Handwritten Digit Recognition using Artificial Neural Networks (ANN)

## Objective
The objective of this assignment is to develop an Artificial Neural Network (ANN) to automate the recognition of handwritten digits (0-9) on postal codes for a postal service organization. 

## Dataset Link
* **Dataset:** MNIST Handwritten Digits Dataset
* **Source:** [Kaggle - MNIST in CSV](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)

## Libraries Used
* **Pandas:** For loading and exploring the dataset.
* **Matplotlib / Seaborn:** For data visualization, displaying sample digits, and plotting evaluation graphs.
* **Scikit-learn:** For splitting the dataset and generating the confusion matrix and classification report.
* **TensorFlow / Keras:** For building, compiling, and training the Artificial Neural Network.
* **NumPy:** For array manipulations and processing predictions.

## Methodology
1. **Data Understanding:** Loaded the MNIST dataset, identified input features and target variables, and visualized a sample digit.
2. **Data Preprocessing:** Checked for missing values, normalized pixel values to a 0-1 range, separated features and targets, applied One-Hot Encoding to the target labels, and split the data into 80% training and 20% testing sets.
3. **Model Development:** Built an ANN using TensorFlow/Keras, compiled it with the Adam optimizer and Categorical Crossentropy loss, and trained it for 10 epochs.
4. **Model Evaluation:** Evaluated the model's performance on the test set using accuracy metrics, a confusion matrix, a classification report, and training vs. validation graphs for both accuracy and loss.

## Model Architecture
The Artificial Neural Network was built with the following architecture:
* **Input Layer:** 784 neurons (flattened 28x28 pixel images).
* **Hidden Layer 1:** 128 Neurons (ReLU activation).
* **Hidden Layer 2:** 64 Neurons (ReLU activation).
* **Output Layer:** 10 Neurons (Softmax activation for 10 digit classes).

## Results
* **Test Accuracy:** 97.57%
* The model successfully learned to distinguish between digits, with the **Confusion Matrix** and **Classification Report** showing high precision and recall across all classes. 
* The **Accuracy vs Epoch** and **Loss vs Epoch** graphs indicate that the model converged effectively over the 10 epochs without significant overfitting.

## Conclusion
The Artificial Neural Network successfully classified MNIST handwritten digits, achieving high test accuracy with minimal misclassifications across all ten classes. The hidden layers in this model were crucial; they enabled the network to learn non-linear patterns and complex hierarchical representations from the raw pixel data, which simple linear models cannot achieve. A key advantage of Deep Learning over traditional Machine Learning demonstrated here is its ability to automatically extract relevant features directly from unstructured data, eliminating the need for manual feature engineering. However, standard ANNs have limitations in image processing tasks. Specifically, they lack spatial awareness because they require flattening the 2D image into a 1D vector, thereby losing the inherent structural relationships between adjacent pixels that architectures like Convolutional Neural Networks (CNNs) preserve. Overall, the model proved highly effective for this automated postal code recognition task.
