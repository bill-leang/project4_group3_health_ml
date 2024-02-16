from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = 'health_ml'

# @app.route("/")
# def hello_world():
#     # file must be in templates folder
#     return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    # get the value nm from login.html
    # age = request.form["ageText"]
    # age =request.form.ageText.data
    age = request.form.get('ageText')
    # print(age)
    # session['exerciseHr'] = request.form["exerciseHr"]
    session['age'] = age
    session['exerciseHr'] = request.form.get('exerciseText')
    return redirect(url_for("user"))
  else:
    return render_template("index.html")

@app.route("/usr", methods=["GET", "POST"])
def user():
    if "age" in session:
       age = session["age"]     
       exerciseHr = session['exerciseHr']
       return f"<h1>prediction = {predict(age, exerciseHr)}</h1>"
    else:
       # if there's no session return to login page
       return redirect(url_for("login"))

def predict(age, exerciseHr ):
   print(type(age))
   return f"You're {age} years old, and you exercise for {exerciseHr} hours per week."

# this is needed
if __name__== '__main__':
    app.run(debug=True)

#in the same folder, > env FLASK_APP=app.py python -m flask run OR >python app.py
# save the file to refresh the server, no need to restart it, because debug=True in app.run()