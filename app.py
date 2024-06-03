from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy user data
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return jsonify({"message": "Logged out"}), 200

@app.route('/status', methods=['GET'])
def status():
    if 'username' in session:
        return jsonify({"message": f"Logged in as {session['username']}"}), 200
    return jsonify({"message": "Not logged in"}), 401

if __name__ == '__main__':
    app.run(debug=True)
