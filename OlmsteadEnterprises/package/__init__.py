from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'c56bec1880b567d61b7cdd462cc2060a'


from package.routes import routes