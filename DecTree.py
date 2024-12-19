#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:44:17 2024

@author: cornelius
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("gender_classification.csv")


#print(df)





label_encoder = LabelEncoder()
df["gender"] = label_encoder.fit_transform(df["gender"])

# features
X = df.drop(columns=['gender'])
# label
y = df['gender']
# Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,
                                                    random_state=42)

# Decision Tree 
decision_tree = DecisionTreeClassifier() # Erzeugung eines Objekts
decision_tree.fit(X_train,y_train) # Trainieren
prediction = decision_tree.predict(X_test) # Vorhersage





accuracy = accuracy_score(y_test, prediction)
print(accuracy)






























