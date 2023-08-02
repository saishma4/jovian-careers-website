from flask import Flask
#instance of class Flask
app = Flask(__name__)

#regestering a route
@app.route("/")
def hello_world():
    return "Hello, Welcome!"

#run usring app.py on a local host
if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)