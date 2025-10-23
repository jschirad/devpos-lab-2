"""
Basic tests for the Flask application
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestFlaskApp(unittest.TestCase):
    """Test cases for Flask application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """Test main endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello from DevOps Lab!')

    def test_health_check(self):
        """Test health endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_info_endpoint(self):
        """Test info endpoint"""
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('app_name', data)

    def test_calculate_endpoint(self):
        """Test calculate endpoint"""
        response = self.app.get('/calculate?x=15&y=20')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('result', data)

if __name__ == '__main__':
    unittest.main()