from django.test import TestCase
from rest_framework.test import APIRequestFactory

from ginger_address_book.views.views import PersonView


class PersonViewTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.obj = PersonView()

    def tearDown(self):
        del self.obj
        del self.factory

    def test_add_person_to_address_book(self):
        request_data = {
            "first_name": "Nabeel",
            "last_name": "T",
            "address": [
                "dwerw we dwd wew",
                "erewr ef edfe "
            ],
            "phone": ["32432432432", "34343322"],
            "email": ["eeef@ded.vom", "defew@fef.vom"]
        }
        view = self.obj.as_view()
        request = self.factory.post('/person/', request_data)
        output = view(request)
        self.assertIsInstance(output, int)
