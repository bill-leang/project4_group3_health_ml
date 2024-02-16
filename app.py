from flask import Flask, redirect, url_for, render_template, request, session
import pandas as pd
import pickle

# To start the server, in terminal, cd to the same folder as this file, > python app.py
# save the file to refresh the server, no need to restart it, because debug=True in app.run()

# Flask Setup
app = Flask(__name__)
app.secret_key = 'health_ml'

# the home page
@app.route("/", methods=["GET", "POST"])
def login():
  # getting the input para after user click Predict button
  if request.method == "POST":
    session['Age'] = request.form.get('ageText')
    session['Exercise Hours Per Week'] = request.form.get('exerciseText')
    session['Sedentary Hours Per Day'] = request.form.get("sedentaryText")
    session['BMI'] = request.form.get('bmiText')
    session['Income'] = request.form.get('incomeText')
    session['Triglycerides'] = request.form.get('triglycerideText')
    session['Cholesterol'] = request.form.get('cholesterolText')
    session['Heart Rate'] = request.form.get('heartRateText')
    return redirect(url_for("prediction"))
  # display the input page
  else:
    return render_template("index.html")

# helper function to return a df from session dictionary
def preprocess(sess):
   df = pd.DataFrame(sess, columns=['Age', 'Cholesterol', 'Heart Rate', 'Exercise Hours Per Week', 'Sedentary Hours Per Day', 'Income', 'BMI',  'Triglycerides'  ], index=[0])
   print(df)
   return df

# page to load after user click Predict
@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    # check if session is populated
    if "Age" in session:
       df = preprocess(session)
       prediction = predict(df)
       return render_template('/predict.html', prediction = prediction )
    else:
       # if there's no session return to input page
       return redirect(url_for("login"))

# load the model from pkl and make prediction
def predict(df ):
  with open('model_noScale.pkl', 'rb') as f:
    rf = pickle.load(f)

  return rf.predict(df)

# this is needed for Flask
if __name__== '__main__':
    app.run(debug=True)

