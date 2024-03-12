import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn import datasets
wine_ds = datasets.load_wine()

wine_df = pd.DataFrame(data=wine_ds.data, columns=wine_ds.feature_names)

print(wine_df)
wine_df["target"] = wine_ds.target

print(wine_df)

# Create a dictionary with the number of samples per each class
label_distribution = {str(label): list(wine_df.target).count(label) for label in set(wine_df.target)}
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

print(wine_df.corr())

from sklearn.model_selection import train_test_split

x = wine_df[['total_phenols', 'flavanoids', 'od280/od315_of_diluted_wines']]
y = wine_df['target'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=100, stratify=y)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()

model_multiclass = model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(y_pred)



from sklearn import metrics

print(metrics.classification_report(y_test, y_pred))

conf_matrix = metrics.confusion_matrix(y_test, y_pred)


sns.heatmap(pd.DataFrame(conf_matrix), cmap="YlGnBu", annot=True, fmt='g')
# plt.show()