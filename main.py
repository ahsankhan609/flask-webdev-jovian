from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 0,
    'title': 'Data Scientist',
    'salary': '150,000',
    'location': 'Lahore, PK',
}, {
    'id': 1,
    'title': 'Data Analyst',
    'salary': '120,000',
    'location': 'Lahore, PK',
}, {
    'id': 2,
    'title': 'Data Engineer',
    'salary': '135,000',
    'location': 'Lahore, PK',
}]


# registering a route
@app.route("/")
# create a view function
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template('home.html', jobs=JOBS)


# Create API route
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


# run app on the replit
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
