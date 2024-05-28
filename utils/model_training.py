import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor

from panda_utils import csv_to_dataframe

conditions_dict = {
    "Partially cloudy": 1,
    "Clear": 2,
    "Overcast": 3,
    "Rain, Partially cloudy": 4,
    "Snow, Partially cloudy": 5,
    "Rain, Overcast": 6,
    "Snow, Overcast": 7,
    "Rain": 8,
    "Snow, Rain, Partially cloudy": 9,
    "Snow": 10,
    "Snow, Rain, Overcast": 11,
    "Snow, Rain, Freezing Drizzle/Freezing Rain, Overcast": 12,
    "Snow, Rain, Ice, Overcast": 13,
    "Snow, Rain, Freezing Drizzle/Freezing Rain, Ice, Partially cloudy": 14,
    "Snow, Rain": 15,
    "Rain, Ice, Overcast": 16,
    "Snow, Rain, Ice, Partially cloudy": 17,
    "Snow, Ice, Overcast": 18
}

# Load the data
full_dataset = csv_to_dataframe('Toronto 1975-01-01 to 2023-12-31.csv')

full_dataset['datetime'] = pd.to_datetime(full_dataset['datetime'])
full_dataset['year'] = full_dataset['datetime'].dt.year
full_dataset['month'] = full_dataset['datetime'].dt.month
full_dataset['day'] = full_dataset['datetime'].dt.day

full_dataset.drop(["name", "stations", "sunrise", "sunset", "description", "icon", "datetime", "preciptype"], axis=1, inplace=True)

full_dataset['conditions'] = full_dataset['conditions'].replace(conditions_dict)
print(full_dataset)
# Separate features (X) and target variable (y)
X = full_dataset.drop(['tempmax', 'tempmin', 'conditions'], axis=1)  # Features

# Choose the target variables
y = full_dataset[['tempmax', 'tempmin', 'conditions']]  # Target variables

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a multi-output regression model with RandomForestRegressor
model = MultiOutputRegressor(RandomForestRegressor())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_test, y_test)
print("Model Score:", score)

joblib.dump(model, 'weather_model.joblib')