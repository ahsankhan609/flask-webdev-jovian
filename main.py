from flask import Flask

app = Flask(__name__)


# registering a route
@app.route("/")
# create a view function
def hello_world():
    return "<p>Hello, World!</p>"


# run app on the replit
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
