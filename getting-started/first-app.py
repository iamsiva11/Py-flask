from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "Home Page"

@app.route("/page2")
def hello():
    return "Welcome to page 2"


if __name__=="__main__":
        app.run(debug=True) #host=""