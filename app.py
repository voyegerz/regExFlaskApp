from flask import Flask, request, render_template
import re

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/regEx", methods=["POST", "GET"])
def matched():
    show = ""
    if request.method == "POST":
        testString = request.form.get("Test-String")
        regEx = request.form.get("RegEx")
        matched = re.findall(regEx, testString)
        if len(matched) == 0:
            show = "no  match found"
        else:
            show = str(matched)
    return render_template("regEx.html", show=show, length=len(matched))


@app.route("/validate_email", methods=["POST", "GET"])
def validate_email():
    validation_result = ""
    if request.method == "POST":
        email = request.form.get("email")
        # Use a simple regex pattern for email validation
        email_pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_pattern, email):
            validation_result = "Valid email address!"
        else:
            validation_result = "Invalid email address! Please enter a valid email."
    return render_template("email_validation.html", validation_result=validation_result)


if __name__ == "__main__":
    app.run(debug=True)
