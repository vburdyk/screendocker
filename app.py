from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! I`m Burdyk Volodymyr</p>"


app.run(host="0.0.0.0", port=5000, debug=True)