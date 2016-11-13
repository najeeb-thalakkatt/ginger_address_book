from django.test import TestCase

from ginger_address_book.services.address_book_service import AddressBookService


class AddressBookServiceTest(TestCase):
    def setUp(self):
        self.obj = AddressBookService()

    def tearDown(self):
        del self.obj

    def test_add_person_to_address_book(self):
        request = {
            "first_name": "Nabeel",
            "last_name": "T",
            "address": [
                "dwerw we dwd wew",
                "erewr ef edfe "
            ],
            "phone": ["32432432432", "34343322"],
            "email": ["eeef@ded.vom", "defew@fef.vom"]
        }
        id = self.obj.add_person_to_address_book(request)
        self.assertIsInstance(id, int)
