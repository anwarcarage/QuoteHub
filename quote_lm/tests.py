from django.test import SimpleTestCase


class MainPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class NewQuoteTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/newquote/")
        self.assertEqual(response.status_code, 200)
