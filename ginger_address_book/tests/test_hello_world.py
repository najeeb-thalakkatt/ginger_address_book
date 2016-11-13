from django.test import TestCase
from rest_framework.test import APIRequestFactory

# from ginger_address_book.views import HelloWord


class HelloWorldTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        # self.obj = HelloWord()

    def tearDown(self):
        # del self.obj
        del self.factory

    def test_hello_api(self):
        expected_output = {'Hello': 'World'}
        # view= HelloWord.as_view()
        request = self.factory.get('/hello_world/')
        # actual_output = view(request)
        self.assertDictEqual(expected_output, "")


