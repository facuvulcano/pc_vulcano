from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = {'destination': ['New York', 'Paris', 'Los Angeles', 'Sydney', 'Tokyo'],
     'budget': [2000, 3000, 4000, 5000, 6000],
     'preference_1': [1, 0, 1, 0, 1],
     'preference_2': [0, 1, 1, 0, 1]
    }

y = {'name': ['Hotel A', 'Hotel B', 'Hotel C', 'Hotel D', 'Hotel E'],
     'price': [1000, 1500, 2000, 2500, 3000],
     'type': ['Luxury', 'Budget', 'Luxury', 'Budget', 'Luxury']
    }


# split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# evaluate the model on the test set
score = model.score(X_test, y_test)

# use the model to make predictions
destination = self.destination_input.text
budget = int(self.budget_input.text)
preferences = self.preferences_input.text.split(',')

# convert the input to the format the model expects
input_data = [destination, budget, preferences]

# make predictions
predictions = model.predict(input_data)

# display the predictions
self.results_label.text = 'Recommendations:\n'
for i, pred in enumerate(predictions):
    self.results_label.text += f'{pred["name"]} - {pred["price"]}\n'
