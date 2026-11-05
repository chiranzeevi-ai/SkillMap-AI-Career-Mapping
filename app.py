
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form.get("name")
    career = request.form.get("career")
    skills = request.form.get("skills")

    return f"""
    <h1>Welcome, {name}!</h1>
    <h2>Your Selected Career: {career}</h2>
    <p>Your Skills: {skills}</p>
    <p>SkillMap assessment received successfully!</p>
    <a href="/">Go Back</a>
    """


if __name__ == "__main__":
    app.run(debug=True)

