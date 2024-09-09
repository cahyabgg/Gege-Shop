from django.test import TestCase,Client


class Accessible(TestCase):
    def default_url_exist(self):
        response = Client.get("")

        self.assertEqual(response.status_code,200)

# Create your tests here.
