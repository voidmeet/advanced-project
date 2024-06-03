import unittest
from payment import app

class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_pay(self):
        response = self.app.post('/pay', json={"amount": 100, "method": "credit_card"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Payment processed", response.data)

    def test_invalid_pay(self):
        response = self.app.post('/pay', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid payment data", response.data)

    def test_payment_status(self):
        self.app.post('/pay', json={"amount": 100, "method": "credit_card"})
        response = self.app.get('/payment-status/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"amount", response.data)

    def test_payment_status_not_found(self):
        response = self.app.get('/payment-status/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Payment not found", response.data)

if __name__ == '__main__':
    unittest.main()
