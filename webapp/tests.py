from django.test import SimpleTestCase


# Create your tests here.
class WebappTest(SimpleTestCase):
    def test_home_view_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_exist(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
