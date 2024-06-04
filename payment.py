from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock payment data
payments = []

@app.route('/pay', methods=['POST'])
def pay():
    payment_data = request.get_json()
    if not payment_data.get('amount') or not payment_data.get('method'):
        return jsonify({"error": "Invalid payment data"}), 400
    
    payment_id = len(payments) + 1
    payment = {
        "id": payment_id,
        "amount": payment_data['amount'],
        "method": payment_data['method']
    }
    payments.append(payment)
    return jsonify({"message": "Payment processed", "payment_id": payment_id}), 200

@app.route('/payment-status/<int:payment_id>', methods=['GET'])
def payment_status(payment_id):
    payment = next((p for p in payments if p['id'] == payment_id), None)
    if not payment:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify(payment), 200

if __name__ == '__main__':
    app.run(debug=True)
