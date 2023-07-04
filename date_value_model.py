import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump
from tensorflow import keras
from sklearn.linear_model import SGDRegressor


# load the data
df = pd.read_csv("./date_value.csv")

print(df.head())

# convert the date to a number (of days since some point)
df["date"] = pd.to_datetime(df["date"])
df["date"] = (df["date"] - df["date"].min()) / pd.Timedelta(1, "D")

# use previous days price to predict next days
df["prev_value"] = df["value"].shift(1)

# drop any rows with missing values
df = df.dropna()

# split into input x and output y
x = df[["date", "prev_value"]]
y = df["value"]

# use 75% of the data for training and 25% for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state= 0)

# train a linear regression model
# model = LinearRegression()

# model = SGDRegressor(max_iter= 1000, tol=1e-3)

# defining the model with keras
model = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=[2]),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(1)
])


# compile the model
model.compile(loss="mean_squared_error", optimizer="adam")

# fit the model
history = model.fit(x_train, y_train, epochs=100, validation_split=0.2)


# model.fit(x_train, y_train)

model.save("model.json")

dump(model, "model.joblib")
# model.save("model", save_format="tfjs")