import unittest
from app import app

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        response = self.app.post('/login', data=dict(username="user1", password="password1"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login successful", response.data)

    def test_invalid_login(self):
        response = self.app.post('/login', data=dict(username="user1", password="wrongpassword"))
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Invalid credentials", response.data)

    def test_status_logged_in(self):
        self.app.post('/login', data=dict(username="user1", password="password1"))
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Logged in as user1", response.data)

    def test_status_not_logged_in(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Not logged in", response.data)

    def test_logout(self):
        self.app.post('/login', data=dict(username="user1", password="password1"))
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Logged out", response.data)

if __name__ == '__main__':
    unittest.main()
