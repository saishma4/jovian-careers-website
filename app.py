from flask import Flask, render_template,jsonify
# instance of class Flask
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs.12,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Banglore',
        'salary': 'Rs.24,00,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': 'Rs.18,00,000'
    }
]
# regestering a route


@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


# run usring app.py on a local host
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
