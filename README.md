# 🎓 Student Score Predictor

A beginner Machine Learning project built with Python and Scikit-Learn that predicts a student's exam score based on:

- Hours Studied
- Attendance Percentage
- Previous Marks

## 🚀 Features

- Reads data from a CSV file

- Trains a Machine Learning model using Linear Regression

- Predicts student scores

- Takes user input

- Displays model accuracy

- Visualizes data using Matplotlib

---

## 📊 Dataset

The dataset contains the following columns:

| Column | Description |
|----------|------------|
| Hours | Hours studied by the student |
| Attendance | Attendance percentage |
| PreviousMarks | Previous exam marks |
| Score | Final exam score |

Example:

```csv
Hours,Attendance,PreviousMarks,Score
2,60,50,55
3,65,55,60
4,70,60,65
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Matplotlib

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/aryanverma11014/Student-Score-Predictor.git
```

Move into the project folder:

```bash
cd Student-Score-Predictor
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib
```

---

## ▶️ Run the Project

```bash
py train.py
```

Example:

```text
Hours studied: 6
Attendance (%): 75
Previous Marks: 62

Predicted Score: 69.53
```

---

## 📈 Graph Visualization

The project also generates a graph showing the relationship between:

- Hours Studied
- Student Score

using Matplotlib.

---

## 🧠 Machine Learning Concept

This project uses **Linear Regression**.

The model learns patterns from historical student data and predicts the most likely score for a new student.

### Training

```python
model.fit(X_train, y_train)
```

### Prediction

```python
model.predict(...)
```

---

## 📁 Project Structure

```text
Student-Score-Predictor/
│
├── data.csv
├── train.py
└── README.md
```

---

## 🎯 Future Improvements

- Larger dataset
- Better visualizations
- Save trained model
- GUI using Tkinter
- Web version using Flask

---

## 👨‍💻 Author

Aryan Verma

GitHub: https://github.com/aryanverma11014
