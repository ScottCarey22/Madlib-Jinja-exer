from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Redirect to homepage"""
    return render_template("base.html")


@app.route("/questions")
def question_form():
    """Generate Question Form"""
    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def make_story():
    """show answers to questions in madlib"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
