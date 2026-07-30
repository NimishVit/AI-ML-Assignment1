# Image Classification using Convolutional Neural Networks (CNN)

## Objective
The objective of this assignment is to develop a Convolutional Neural Network (CNN) model to automate the accurate classification of pet images into Cats and Dogs for an animal welfare organization.

## Dataset Link
* **Dataset:** Cats vs Dogs Dataset
* **Kaggle Link:** [https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset](https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset)

## Libraries Used
* **TensorFlow / Keras:** For building, compiling, and training the CNN model and data generators.
* **Matplotlib & Seaborn:** For image visualization and plotting evaluation graphs (accuracy/loss, confusion matrix).
* **Scikit-learn:** For calculating evaluation metrics (Precision, Recall, F1-Score, Confusion Matrix).
* **OS & Glob:** For directory traversal and file handling.
* **NumPy:** For array and prediction manipulations.

## Methodology
1. **Data Understanding:** Explored the dataset's folder structure, visualized sample cat and dog images, and identified basic properties like image dimensions and total classes.
2. **Data Preprocessing:** Used `ImageDataGenerator` to rescale pixel values to the 0-1 range, resize all images to 128x128 pixels, and split the dataset into an 80% training set and a 20% testing/validation set.
3. **Model Development:** Designed a CNN with three consecutive Convolutional and MaxPooling blocks to extract features, followed by a Flatten layer and Dense layers for classification. The model was compiled with the Adam optimizer and Binary Crossentropy loss, then trained for 10 epochs.
4. **Model Evaluation:** Evaluated the test set using Accuracy, Precision, Recall, and F1-Score. Generated a confusion matrix and plotted Accuracy vs. Epoch and Loss vs. Epoch to analyze the learning process.

## CNN Architecture
The architecture of the Convolutional Neural Network is as follows
* **Input Layer:** 128x128x3 images
* **Layer 1:** Conv2D (32 filters, 3x3, ReLU) followed by MaxPooling2D (2x2)
* **Layer 2:** Conv2D (64 filters, 3x3, ReLU) followed by MaxPooling2D (2x2)
* **Layer 3:** Conv2D (128 filters, 3x3, ReLU) followed by MaxPooling2D (2x2)
* **Flatten Layer:** Converts the 2D feature maps to a 1D vector
* **Hidden Dense Layer:** 128 neurons (ReLU)
* **Output Layer:** 1 neuron (Sigmoid activation for binary classification)

## Results
* The model learned to effectively distinguish between cats and dogs, converging well over the 10 epochs.
* The evaluation metrics (Test Accuracy, Precision, Recall, F1-Score) and Confusion Matrix confirmed the model's predictive capability and balanced performance across both classes.

## Conclusion
The Convolutional Neural Network (CNN) demonstrated highly effective performance in automating the classification of pet images into Cats and Dogs. A key finding is that the model achieved strong validation accuracy, validating the robustness of CNNs for image-based binary classification. The architecture's convolution layers were critical for automatically extracting spatial features like edges and textures, while pooling layers reduced the dimensionality and computational load, preventing overfitting. A primary advantage of CNNs over standard Artificial Neural Networks (ANNs) for image classification is their ability to preserve the two-dimensional spatial relationships between pixels, whereas ANNs require flattening the image initially, losing this structural context. However, a notable limitation of CNNs is their demand for substantial computational resources and large training datasets to learn effectively without overfitting.
