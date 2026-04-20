from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "مرحباً بك في API عثمان الخاص!"

@app.route('/bio')
def get_bio():
    return jsonify({"name": "OTHMANE", "status": "Online", "team": "H4X_TEAM"})

if __name__ == "__main__":
    app.run()
