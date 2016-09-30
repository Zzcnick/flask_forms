# Flask App for Forms

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

# Website Routes
# ===============================================================
@app.route("/", methods=["GET"])
def index():
    print request.form, "\n===================================\n"
    return render_template("form.html",
                           title="A Form")

@app.route("/authenticate/", methods=["POST"]) 
def auth():
    if verify(request.form) > 0:
        return render_template("auth.html",
                               status="Success!")
    return render_template("auth.html",
                           status="Failure!")

# Login Mechanism - To Be Replaced
# ===============================================================
def verify(form):
    if (form["username"] == "Foo" and
        form["password"] == "bar"):
        return 1
    return -1

# Prevents following code from running unless it is standalone.
# ===============================================================
if (__name__ == "__main__"):
    app.debug = True
    app.run()
