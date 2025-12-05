import unittest
from board import create_app

class TestPagesBlueprint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b"<h1>Home</h1>", response.data)

    def test_about_route(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b"<h1>About</h1>", response.data) 

if __name__ == "__main__":
    unittest.main()

