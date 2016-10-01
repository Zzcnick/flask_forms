# Flask App for Forms

from flask import Flask, render_template, redirect, request
from utils import authenticate
app = Flask(__name__)

# Website Routes
# ===============================================================
@app.route("/", methods=["GET"])
def index():
    print request.form, "\n===================================\n" # Debugging
    return render_template("form.html",
                           title="Login")

@app.route("/login/", methods=["POST", "GET"]) 
def auth():
    print request.form, "\n===================================\n" # Debugging
    try:
        action = request.form["action"]
    except:
        return render_template("form.html",
                               title="Login")
    if action == "Login":
        return login(request.form["username"],request.form["password"])
    if action == "Register":
        return register(request.form["username"],request.form["password"])
    
# Formatting - Should this be in authenticate? 
# ===============================================================
def login(username,password):
    logstatus = authenticate.verify(username,password)
    if logstatus > 0:
        return render_template("form.html",
                               title="Login",
                               status="Login Success!")
    elif logstatus == -1:
        return render_template("form.html",
                               title="Login",
                               status="Login Failed: Unknown Error!")
    elif logstatus == -2:
        return render_template("form.html",
                               title="Login",
                               status="Login Failed: User does not exist.")

def register(username,password):
    regstatus = authenticate.register(username,password)
    if regstatus > 0:
        return render_template("form.html",
                               title="Login",
                               status="Registration Success!")                    
    elif regstatus == -1:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Username already exists.")                    
    elif regstatus == -2:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Invalid username.")
    elif regstatus == -3:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Password too short.")
    elif regstatus == -4:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Chill with your password length, eh?")
    elif regstatus == -5:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Username too short.")
    elif regstatus == -6:
        return render_template("form.html", 
                               title="Login",
                               status="Registration Failed: Surely you can choose a shorter name to identify yourself.")

# Prevents following code from running unless it is standalone.
# ===============================================================
if (__name__ == "__main__"):
    app.debug = True
    app.run()
