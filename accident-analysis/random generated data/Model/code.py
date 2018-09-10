#Preprocessing

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data = pd.read_csv('data.csv')
for column in data.columns:
    data[column] = le.fit_transform(data[column])

labels = data['Incident Type']
data.drop('Incident Type', axis=1, inplace=True)

train, cv, target, target_cv = train_test_split(data, labels, test_size=0.08)

#Model

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

clf = MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(100,), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)

clf.fit(train, target)

predictions_train = clf.predict(train)
predictions_cv = clf.predict(cv)

print('Train Score: ', accuracy_score(target, predictions_train))
print('CV Score: ', accuracy_score(target_cv, predictions_cv))


