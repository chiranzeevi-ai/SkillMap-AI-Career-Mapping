
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to SkillMap</h1>
    <p>Intelligent Skill Gap and Career Mapping System</p>
    <p>Your career journey starts here!</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
