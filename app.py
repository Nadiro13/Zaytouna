from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    return render_template("home.html")

@app.route("/test1")
def test1():
    return render_template("test1.html")


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()

