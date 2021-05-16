from flask_testing import TestCase
from api.app import create_app


class MainTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_app(self):
        self.assertIsNotNone(create_app)
