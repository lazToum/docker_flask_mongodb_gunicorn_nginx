from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['DEBUG'] = True
SECRET_KEY = 'gfdafg$#r345fvsg&*r435fga0vvk0kvf#$#tr4fbadfbf?vfav[?>V.Vd.>vregreDxvx='
app.config['SECRET_KEY'] = SECRET_KEY
app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY

app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskDb',
    'username': 'flaskUser',
    'password': 'changeMe',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
