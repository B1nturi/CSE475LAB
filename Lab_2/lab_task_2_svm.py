# -*- coding: utf-8 -*-
"""Lab_Task_2_SVM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F6psxYYVjMHvTUA6wzsddqWOKGOg0DMy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error,classification_report

df = pd.read_csv('/content/drive/MyDrive/CSE475/Lab_02/Drivers License Data.csv')
df

df.head()

df.tail()

df.isnull().sum()

df.info()

mode_value = df['Training'].mode()[0]
mode_value

df['Training'] = df['Training'].fillna(mode_value)

df

# df.dropna(inplace=True)
df.isnull().sum()

df.duplicated().sum()

df_copy = df.copy()

df['Gender'].value_counts()

# Define the mapping dictionary
gender_mapping = {
    'Male': 1,
    'Female': 2,
}

# Apply the mapping
df['Gender'] = df['Gender'].map(gender_mapping)

df['Age Group'].value_counts()

# Define the mapping dictionary
ageGroup_mapping = {
    'Young Adult': 1,
    'Middle Age': 2,
    'Teenager': 3
}

# Apply the mapping
df['Age Group'] = df['Age Group'].map(ageGroup_mapping)

df['Race'].value_counts()

# Define the mapping dictionary
race_mapping = {
    'White': 1,
    'Black': 2,
    'Other': 3
}

# Apply the mapping
df['Race'] = df['Race'].map(race_mapping)

df['Training'].value_counts()

# Define the mapping dictionary
training_mapping = {
    'Basic': 1,
    'Advanced': 2,
}

# Apply the mapping
df['Training'] = df['Training'].map(training_mapping)

df['Reactions'].value_counts()

# Define the mapping dictionary
reaction_mapping = {
    'Average': 1,
    'Fast': 2,
    'Slow': 3
}

# Apply the mapping
df['Reactions'] = df['Reactions'].map(reaction_mapping)

df['Qualified'].value_counts()

# Define the mapping dictionary
qualified_mapping = {
    'No': 0,
    'Yes': 1,
}

# Apply the mapping
df['Qualified'] = df['Qualified'].map(qualified_mapping)

df

# Counting the number of males and females
gender_counts = df_copy['Gender'].value_counts()
gender_counts

# Create a pie chart
plt.figure(figsize=(6, 6))  # Set the figure size
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Gender Distribution')

# Show the pie chart
plt.show()

sns.countplot(x='Qualified', data=df_copy, palette='viridis')
plt.title('Qualified vs Disqualified Drivers License')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='Training', y='Confidence', hue='Gender', data=df_copy)

# Add a title and labels
plt.title('Confidence Distribution by Gender and Training')
plt.xlabel('Training')
plt.ylabel('Confidence')


# Display the plot
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df_copy['Speed Control'], bins=30, edgecolor='black')

# Add a title and labels
plt.title('Distribution of Speed Control')
plt.xlabel('Speed Control')
plt.ylabel('Frequency')

# Display the plot
plt.show()

df.drop(columns=['Applicant ID'],inplace=True)

df

correlation = df.corr()
correlation

plt.figure(figsize=(12,8), dpi=77)
sns.heatmap(correlation, linecolor='white',linewidths=0.1, annot=True)
plt.title('Correlation Matrix'.upper(), size=19, pad=13)
plt.xlabel('Drivers License Data')
plt.ylabel('Drivers License Data')
plt.xticks(rotation=33)
plt.show()

X=df.drop(columns=['Qualified'])
Y=df['Qualified']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

"""# **SVM**"""

from sklearn.svm import SVC

# Initialize the SVM model (with a linear kernel)

#A linear kernel in Support Vector Machines (SVM) is the simplest kernel function, used when the data is linearly separable.
#random_state=42: Ensures reproducibility of results.

model = SVC(kernel='rbf', C=0.5, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

print(y_pred)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# Calculate recall (sensitivity)
recall = recall_score(y_test, y_pred)
print("Recall (Sensitivity):", recall)

# Calculate F1-score
f1 = f1_score(y_test, y_pred)
print("F1-Score:", f1)

#confuison matrix
import matplotlib.pyplot as plt
from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(y_test,y_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Negative', 'Positive'])
cm_display.plot()
plt.show()