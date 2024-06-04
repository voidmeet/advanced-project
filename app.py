from flask import Flask, request, jsonify, render_template, session
import config  # Import the configuration file

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # This is needed for session management

# Dummy user data for login
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    return render_template('index.html')

# Check if the login feature is turned on using the config file
if config.USER_AUTHENTICATION_ENABLED:
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

# Check if the payment feature is turned on using the config file
if config.PAYMENT_INTEGRATION_ENABLED:
    @app.route('/payment', methods=['POST'])
    def process_payment():
        # Handle payment processing logic here
        return jsonify({"message": "Payment processed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

