import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Load the dataset
#Titanic - Machine Learning from Disaster from kaggle.com
data = pd.read_csv('train.csv')
print(data.info(),'\n')
# Define the target column and feature columns
target_column = 'Survived'
feature_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'] #List of the columns to be used as features for prediction.
# Encode categorical features
label_encoder = LabelEncoder()
data['Sex'] = label_encoder.fit_transform(data['Sex'])
data['Embarked'] = label_encoder.fit_transform(data['Embarked'])
# Handle missing values
data['Age'].fillna(data['Age'].median())
data['Fare'].fillna(data['Fare'].median())
# Define features and target
X = data[feature_columns]
Y = data[target_column]
# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Create and train a Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, Y_train)
# Make predictions and calculate accuracy
Y_pred = clf.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy:.2f}")
# Visualize and interpret the generated decision tree
plt.figure(figsize=(30, 25), dpi=100)
plot_tree(clf, filled=True, feature_names=feature_columns, class_names=['Not Survived', 'Survived'])
plt.title('Decision Tree Visualization\nTitanic Passenger Survival Predication')
plt.show()
