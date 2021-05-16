from flask_testing import TestCase
from api.app import create_app


class MainTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_app(self):
        self.assertIsNotNone(create_app)

    def test_authorized_key_must_return_403(self):
        response = self.client.get("/api/v1/users/verify")
        self.assertEqual(response.status_code, 403)