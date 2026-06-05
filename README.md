# Student Score Predictor

A beginner-friendly machine learning project that predicts a student's final exam score using study hours, attendance percentage, and previous marks.

## Overview

This project demonstrates the basic ML workflow: loading a dataset, selecting features, splitting training/testing data, training a Linear Regression model, checking model score, taking user input, making a prediction, and visualizing the data.

## Tech Stack

- Python
- Pandas
- Scikit-Learn
- Matplotlib

## Features

- Reads student data from a CSV file
- Trains a Linear Regression model
- Predicts a student's final score from user input
- Displays model score on test data
- Prints learned coefficients
- Visualizes the relationship between hours studied and score

## Dataset

The dataset uses four columns:

| Column | Description |
| --- | --- |
| `Hours` | Number of hours studied |
| `Attendance` | Attendance percentage |
| `PreviousMarks` | Previous exam marks |
| `Score` | Final exam score |

Example:

```csv
Hours,Attendance,PreviousMarks,Score
2,60,50,55
3,65,55,60
4,70,60,65
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/aryanverma11014/Student-Score-Predictor.git
cd Student-Score-Predictor
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib
```

Run the project:

```bash
py train.py
```

On macOS/Linux, use:

```bash
python train.py
```

## Sample Output

```text
model accuracy: 97.42%

learned Coefficients:
[1.23 0.45 0.67]

Hours studied: 6
attendance (%): 75
previous Marks: 62

Predicted Score: 69.53
```

The exact accuracy and coefficients may change as the dataset changes.

## Visualization

The script generates a Matplotlib chart for:

```text
Hours Studied vs Score
```

Suggested screenshot to add later:

```text
/screenshots/hours-vs-score.png
```

## Machine Learning Concept

This project uses Linear Regression. The model learns the relationship between the input features and final score, then predicts the likely score for a new student.

Training step:

```python
model.fit(x_train, y_train)
```

Prediction step:

```python
model.predict([[Hours, Attendance, Previous_marks]])
```

## Project Structure

```text
Student-Score-Predictor/
├── data.csv
├── train.py
└── README.md
```

## What I Learned

- Loading and preparing CSV data with Pandas
- Splitting data into training and testing sets
- Training a basic Scikit-Learn regression model
- Taking user input for ML predictions
- Creating a simple visualization with Matplotlib

## Future Improvements

- Add a larger and more realistic dataset
- Save the trained model with `joblib` or `pickle`
- Add a `requirements.txt` file
- Add better charts and screenshots
- Turn the model into a Flask or FastAPI prediction API
- Build a simple web UI for predictions

## Author

Aryan Verma

GitHub: https://github.com/aryanverma11014
