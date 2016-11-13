"""
Serializers are used to convert the model data to JSON.
"""

from rest_framework import serializers

from ginger_address_book.models.models import Person, Address, Email, Phone, Group, GroupMemebers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_str')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email_str')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone_str')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        addresses = AddressSerializer(read_only=True, many=True)
        email_addresses = EmailSerializer(read_only=True, many=True)
        phone_numbers = PhoneSerializer(read_only=True, many=True)
        fields = ('first_name', 'last_name', 'addresses', 'email_addresses', 'phone_numbers')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        group_members = PersonSerializer(read_only=True, many=True)
        fields = ('group_name', 'group_members')


class PersonGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMemebers
        fields = ('group_id', 'person_id')
