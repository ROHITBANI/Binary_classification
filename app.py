from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('medical_expense_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to predict medical expenses
def predict_medical_expenses(age, smoke, bmi, gender, region):
    # Preprocess the input values if needed
    # Make predictions using the trained model
    # Replace the following line with your actual prediction code
    predicted_expense = 5000  # Dummy prediction for illustration
    return predicted_expense

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    age = int(request.form['age'])
    smoke = request.form['smoke']
    bmi = float(request.form['bmi'])
    gender = request.form['gender']
    region = request.form['region']
    
    # Convert smoke and gender values to binary
    smoke_binary = 1 if smoke.lower() == 'yes' else 0
    gender_binary = 1 if gender.lower() == 'male' else 0
    
    # Make prediction
    predicted_expense = predict_medical_expenses(age, smoke_binary, bmi, gender_binary, region)
    
    # Render the result template with the prediction
    return render_template('result.html', predicted_expense=predicted_expense)

if __name__ == '__main__':
    app.run(debug=True)
