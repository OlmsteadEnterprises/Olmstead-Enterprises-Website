from package import app
from flask import render_template, redirect


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("Home.html")