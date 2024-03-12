import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
iris_ds = datasets.load_iris()

# print(iris_ds.summary)

iris_df = pd.DataFrame(data= iris_ds.data, columns=iris_ds.feature_names)
iris_df["target"] = iris_ds.target

print(iris_df)

# Create a dictionary with the number of samples per each class
label_distribution = {str(label): list(iris_df.target).count(label) for label in set(iris_df.target)}
labels = list(label_distribution.keys())
values = list(label_distribution.values())
print("Class distribution (class: n° of samples):", label_distribution)
 
fig = plt.figure()

# creating the bar plot
plt.bar(labels, values)

plt.xlabel("Label")
plt.ylabel("N° of samples")
plt.title("Dataset distribution")
# plt.show()

class2delete = iris_df[iris_df.target == 2].index
print(class2delete)

# inplace=True
iris_df_binary = iris_df.drop(class2delete)
print(iris_df_binary)

sns.heatmap(iris_df_binary.corr(), cmap="YlGnBu", annot=True)
# plt.show()

from sklearn.model_selection import train_test_split

x = iris_df_binary[['petal length (cm)', 'petal width (cm)']].values
y = iris_df_binary['target'].values


print(len(y))
print(y[0])

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10, stratify=y)

from sklearn import svm

model = svm.SVC()

# print(model.summary)

model_binary = model.fit(x_train, y_train)

y_pred = model_binary.predict(x_test)

print(y_pred)

