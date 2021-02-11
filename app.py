from flask import Flask, request

# create and initialize a new Flask app
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_seed():
    with open("num.txt", "r") as f:
        seed = f.read()
    return str(seed)


@app.route("/", methods=["POST"])
def save_seed():
    data = request.get_json()
    seed = data.get('num')
    with open("num.txt", "w") as f:
        f.write(str(seed))
    return str(seed)


if __name__ == "__main__":
    app.run(host='0.0.0.0')