from flask import Flask, render_template, request
import joblib 
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the saved Lasso model
model = joblib.load('lasso_model.joblib')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        study_hours = float(request.form['study_hours'])
        attendance_rate = float(request.form['attendance_rate'])
        previous_exam_scores = float(request.form['previous_exam_scores'])
        assignments_completed = float(request.form['assignments_completed'])
        extracurricular_participation = float(request.form['extracurricular_participation'])

        # Arrange data into a numpy array
        input_data = np.array([[study_hours, attendance_rate, previous_exam_scores, assignments_completed, extracurricular_participation]])

        # Predict using the Lasso model
        prediction = model.predict(input_data)[0]

        return render_template('index.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
