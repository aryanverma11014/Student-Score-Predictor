import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# load the dataset
data = pd.read_csv("data.csv")

#input columns (features)

x = data[["Hours", "Attendance", "PreviousMarks"]]

#output column (target)

y = data["Score"]

#split data into training and testing 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#create the model
model = LinearRegression()

#train the model
model.fit(x_train, y_train)

#check accuracy of the model
accuracy = model.score(x_test, y_test)
print(f"\nmodel accuracy: {accuracy * 100:.2f}%")

#shows learn values 
print("\nlearned Coefficients:")
print(model.coef_)

#take user input
Hours = float(input("\nHours studied"))
Attendance = float(input('attendance (%):'))
Previous_marks = float(input("previous Marks:"))

#predict score
prediction = model.predict([[Hours, Attendance, Previous_marks]])

print(f"\nPredicted Score: {prediction[0]:.2f}")

#plot the data
plt.figure(figsize=(8,5))
plt.scatter(data["Hours"], data["Score"])
plt.plot(data["Hours"], data["Score"])

plt.title("Hours studied vs Score")
plt.xlabel("Hours studied")
plt.ylabel("Score")

plt.grid(True)
plt.show()