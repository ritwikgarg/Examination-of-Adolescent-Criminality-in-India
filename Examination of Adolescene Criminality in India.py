# -*- coding: utf-8 -*-
"""Examination-of-Adolescent-Criminality-in-India.ipynb

Automatically generated by Colaboratory.
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from mlxtend.plotting import plot_decision_regions

dataset = pd.read_csv('DMP11_Dataset.csv')
feature_columns = ['Education_Illiterate', 'Education_Upto_primary', 'Education_Above_Primary_but_below_Higher_Secondary', 'Education_Higher_Secondary_&_above','Total_Juvenile_Crimes', 'Crime_Score']
X = dataset[feature_columns].values
y = dataset['Required_Awarenss_Level'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifiersvc = SVC(kernel = 'linear',random_state=0)
classifiersvc.fit(X_train, y_train)
y_predsvc = classifiersvc.predict(X_test)

from sklearn.ensemble import RandomForestClassifier
classifierrf = RandomForestClassifier(n_estimators = 10, criterion = 'entropy',random_state=42)
classifierrf.fit(X_train, y_train)
y_predrf = classifierrf.predict(X_test)

classifierknn = KNeighborsClassifier(n_neighbors=5)
classifierknn.fit(X_train, y_train)
y_predknn = classifierknn.predict(X_test)

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
print("This is for SVM.\n\n")
cmsvc = confusion_matrix(y_test, y_predsvc)
print(cmsvc)
print(classification_report(y_test, y_predsvc))
accuracy = accuracy_score(y_test, y_predsvc)*100
print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')
print("\n\n")
print("This is for Random Forest Classification.\n\n")
cmrf = confusion_matrix(y_test, y_predrf)
print(cmrf)
print(classification_report(y_test, y_predrf))
accuracy = accuracy_score(y_test, y_predrf)*100
print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')
print("\n\n")
print("This is for KNN.\n\n")
cmknn = confusion_matrix(y_test, y_predknn)
print(cmknn)
print(classification_report(y_test, y_predknn))
accuracy = accuracy_score(y_test, y_predknn)*100
print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')
print("\n\n")

print("This is for KNN Classifier\n\n")
plt.rcParams.update(plt.rcParamsDefault)
cmknn_df = pd.DataFrame(cmknn,
                     index = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'], 
                     columns = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'])

sns.heatmap(cmknn_df, annot=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print("\n\n")

print("This is for Random Forest Classifier\n\n")
plt.rcParams.update(plt.rcParamsDefault)
cmrf_df = pd.DataFrame(cmrf,
                     index = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'], 
                     columns = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'])

sns.heatmap(cmrf_df, annot=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print("\n\n")

print("This is for SVM Classifier\n\n")
plt.rcParams.update(plt.rcParamsDefault)
cmsvc_df = pd.DataFrame(cmsvc,
                     index = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'], 
                     columns = ['Relaxed-Awareness-Required', 'Focused-Awareness-Required', 'High-Awareness-Required', 'Alarmingly-High-Awareness-Required'])

sns.heatmap(cmsvc_df, annot=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print("\n\n")
