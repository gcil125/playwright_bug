from flask import request, Flask

app = Flask(__name__)


@app.route("/headers", methods=["GET", "POST", "PUT", "DELETE"])
def header():
    print(f"request body is :{request.get_json()}")
    return request.get_json()


if __name__ == "__main__":
    app.run(debug=True)
