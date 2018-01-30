from app import app
import unittest

# Testing the status code
class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/car/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        
if __name__ == "__main__":
    unittest.main()