import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split


cancer_ds = datasets.load_breast_cancer()

print(cancer_ds)

cancer_ds_df = pd.DataFrame(data=cancer_ds.data, columns=cancer_ds.feature_names)
cancer_ds_df['target'] = cancer_ds.target


print(cancer_ds)
print(cancer_ds_df.head())

label_distribution = cancer_ds_df['target'].value_counts().to_dict()
labels = list(label_distribution.keys())
values = list(label_distribution.values())
print("Class distribution (class: n° of samples):", label_distribution)

plt.bar(labels, values)

plt.ylabel("label")
plt.xlabel("no of samples")
plt.title("Dataset distribution")
# plt.show()


# from sklearn.model_selection import train_test_split

x = cancer_ds_df[['mean radius','mean perimeter','mean area','mean compactness','mean concave points']]
y = cancer_ds_df['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(x_train.shape)
print(y_train.shape)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(random_state= 42)
# y_train = y_train.flatten()
logreg.fit(x_train, y_train)

y_pred = logreg.predict(x_test)

print(y_pred)