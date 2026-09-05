import os
from flask import Flask, jsonify

app = Flask(__name__)

# Biến đếm toàn cục lưu trong RAM
counter_value = 0


@app.route("/")
def home():
    return "Flask App running on Render PaaS!"


@app.route("/api/counter")
def counter():
    global counter_value
    counter_value += 1
    return jsonify({"counter": counter_value})


@app.route("/api/info")
def info():
    student_name = os.environ.get("STUDENT_NAME", "Default Name")
    return jsonify({"student_name": student_name})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)