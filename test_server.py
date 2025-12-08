from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test_start.html")

@app.route("/api/test_start")
def api_test_start():
    name = request.args.get("name", "Anonymous")
    data = {
        "name": name,
        "hp": 100,
        "fuel": 50,
        "location": "TEST_AIRPORT"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
