from flask import Flask 


api = Flask(__name__)


@api.route("/")
def home():
    return "Home page"


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000)
