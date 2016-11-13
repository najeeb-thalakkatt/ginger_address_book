
"""
Module level doc
"""
from ginger_address_book.models.models import Person, Address, Phone, Email, Group, GroupMemebers
from ginger_address_book.serializers.addressbook_serializer import PersonSerializer, GroupSerializer, \
    PersonGroupSerializer


class AddressBookService(object):

    """
    This service class will deals with the business logic of the project
    """

    def __init__(self):
        pass

    def add_person_to_address_book(self, data):
        """
        Add a person to the address book.
        """
        # required comments which explains your logic
        person = Person(
            first_name=data['first_name'], last_name=data['last_name'])
        person.save()
        for i in data['address']:
            ad = Address(address_str=i)
            ad.save()
            person.addresses.add(ad)
        for i in data['email']:
            email = Email(email_str=i)
            email.save()
            person.email_addresses.add(email)
        for i in data['phone']:
            phone = Phone(phone_str=i)
            phone.save()
            person.phone_numbers.add(phone)
        return person.id

    def get_person_details_by_id(self, id):
        """
        Get details of a person
        """
        person_dict = {}
        person = Person.objects.get(id=int(id))
        adds = person.addresses.values()
        phone_numbers = person.phone_numbers.values()
        email_address = person.email_addresses.values()
        ps = PersonSerializer(person).data
        person_dict['first_name'] = ps['first_name']
        person_dict['lat_name'] = ps['last_name']
        person_dict['addresses'] = adds
        person_dict['phone_numbers'] = phone_numbers
        person_dict['email_address'] = email_address
        return person_dict

    def add_group_to_address_book(self, group_details):
        """
        Add a group to the address book.
        """
        group = Group(group_name=group_details['group_name'])
        group.save()
        return group.id

    def get_group_details_by_id(self, id):
        """
        Given a group we want to easily find its members.
        """
        group = Group.objects.get(id=int(id))
        group_dict = {}
        group_serializer = GroupSerializer(group).data
        group_dict['group_name'] = group_serializer['group_name']
        group_dict['group_members'] = group.group_members.values()
        return group_dict

    def add_members_to_group(self, id, memeber_data):
        """
        Adding members to a group
        """
        group = Group.objects.get(id=int(id))
        add_list = memeber_data['add_list']
        for i in add_list:
            person = Person.objects.get(id=int((i)))
            group.group_members.add(person)

    def find_group_by_members(self, id):
        """
        Given a person we want to easily find the groups the person belongs to.
        """
        query = "SELECT * from group_group_members where person_id = {person_id}".format(
            person_id=id)
        group_details = GroupMemebers.objects.raw(query)
        detail_list = []
        for group_detail in group_details:
            person_group_serializer = PersonGroupSerializer(group_detail).data
            group = Group.objects.get(id=person_group_serializer['group_id'])
            group_ser = GroupSerializer(group)
            detail_list.append(group_ser.data)
        return detail_list

    def find_person_by_name(self, search_str):
        """
        Find person by name (can supply either first name, last name, or both).
        """
        search_list = []
        query_first_name = "SELECT * FROM person WHERE first_name LIKE '%{search_str}%'".format(
            search_str=search_str)
        persons_f_name = Person.objects.raw(query_first_name)
        for profile in persons_f_name:
            person_ser = PersonSerializer(profile)
            search_list.append(person_ser.data)
        query_last_name = "SELECT * FROM person WHERE last_name LIKE '%{search_str}%'".format(
            search_str=search_str)
        persons_l_name = Person.objects.raw(query_last_name)
        for profile in persons_l_name:
            person_ser = PersonSerializer(profile)
            search_list.append(person_ser.data)
        return search_list
