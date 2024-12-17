# 8. Naive Bayes with Categorized Spending Score

# Step 1: Import necessary libraries
from google.colab import files
uploaded = files.upload()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Step 2: Load the dataset
dataset = pd.read_csv('Mall_Customers.csv')

# Step 3: Prepare the data
# Extracting independent variables (Age and Annual Income)
x = dataset.iloc[:, [2, 3]].values  # Features: Age and Annual Income
# Categorizing the Spending Score (1-100) into three classes: Low, Medium, High
y = dataset.iloc[:, 4].values  # Spending Score

# Categorizing Spending Score:
# Create a new column 'Spending_Category' based on Spending Score
y_categories = []
for score in y:
    if score < 40:
        y_categories.append('Low')
    elif 40 <= score < 70:
        y_categories.append('Medium')
    else:
        y_categories.append('High')

# Convert y_categories to a pandas series
y = pd.Series(y_categories)

# Step 4: Splitting the dataset into Training and Testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# Step 5: Feature Scaling
# It's important to scale the data when using algorithms like Naive Bayes
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Step 6: Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# Step 7: Predicting the Test set results
y_pred = classifier.predict(x_test)

# Step 8: Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Step 9: Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Step 10: Display the results
print("Confusion Matrix:")
print(cm)

print(f"\nAccuracy of the Naive Bayes model: {accuracy * 100:.2f}%")
