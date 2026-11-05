
from flask import Flask, render_template
from flask import request

from models.skill_analyzer import analyze_skills

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form.get("name", "").strip()
    career = request.form.get("career", "").strip()
    skills = request.form.get("skills", "").strip()

    if not name or not skills:
        return "Please enter your name and skills.", 400

    try:
        result = analyze_skills(career, skills)
    except ValueError:
        return "Invalid career selection.", 400

    return render_template(
        "result.html",
        name=name,
        career=career,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
