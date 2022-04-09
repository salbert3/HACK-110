from cProfile import label
from flask import Flask, render_template, render_template_string, request
from helpers import todo

app: Flask = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form["class"] == "Tuesday, Thursday":
            variable_two = request.form["course"]
            return render_template('success.html',variable_two=variable_two)
        else:
            variable = request.form["course"]
            return render_template('success.html',variable=variable)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
