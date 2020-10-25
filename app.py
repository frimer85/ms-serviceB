from flask import Flask

# Initializing Flask App
app = Flask(__name__)

@app.route('/service-B')
def hello():
    return 'Service-B says: Hello World'


if __name__ == "__main__":
    app.run(host='0.0.0.0')