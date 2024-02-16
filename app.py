from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # file must be in templates folder
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    # get the value nm from login.html
    age = request.form["age"]
    return redirect(url_for("user", age=age))
  else:
    return render_template("login.html")

@app.route("/<age>")
def user(age):
    return f"<h1>prediction = {predict(age)}</h1>"

def predict(age ):
   return age*365

# this is needed
if __name__== '__main__':
    app.run(debug=True)

#in the same folder, > env FLASK_APP=app.py python -m flask run OR >python app.py
# save the file to refresh the server, no need to restart it, because debug=True in app.run()