from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>"

# will be able to use <name> in code
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# using redirect
@app.route("/admin")
def admin():
    # use the function name in url_for
    # return redirect(url_for("hello_world"))

    # passing an argument in url_for
    return redirect(url_for("user",name="Admin!"))

# this is needed
if __name__== '__main__':
    app.run(debug=True)

#in the same folder, > env FLASK_APP=app.py python -m flask run OR >python app.py
# save the file to refresh the server, no need to restart it.