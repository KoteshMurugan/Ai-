from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix

# Load the dataset
data_set = pd.read_csv('Mall_Customers.csv')

# Extract features and target variable
x = data_set[['Age', 'Annual Income (k$)']].values

# Categorize 'Spending Score (1-100)' into Low, Medium, High
y = pd.cut(data_set['Spending Score (1-100)'], bins=[0, 33, 66, 100], labels=['Low', 'Medium', 'High'])

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Fit Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)

# Predict on test data
y_pred = classifier.predict(x_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Plotting the Decision Tree
plt.figure(figsize=(12,8))
plot_tree(classifier, filled=True, feature_names=['Age', 'Annual Income'], class_names=['Low', 'Medium', 'High'])
plt.title("Decision Tree for Customer Segmentation")
plt.show()
