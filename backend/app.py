from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = "mongodb+srv://mlops:mlops@cluster0.owb805b.mongodb.net/"
mongo = PyMongo(app)

@app.route('/submit', methods=['POST'])
def submit():
    user_info = request.json
    mongo.db.users.insert_one(user_info)
    return jsonify(message="User info stored successfully"), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
