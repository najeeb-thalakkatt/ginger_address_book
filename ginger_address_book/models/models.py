"""
These are Models, they are used to interact with the Database.

"""

from django.db import models


class Address(models.Model):
    address_str = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'address'


class Phone(models.Model):
    phone_str = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'phone'


class Email(models.Model):
    email_str = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'email'


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    addresses = models.ManyToManyField(Address)
    phone_numbers = models.ManyToManyField(Phone)
    email_addresses = models.ManyToManyField(Email)

    class Meta:
        managed = True
        db_table = 'person'


class Group(models.Model):
    group_name = models.CharField(max_length=30)
    group_members = models.ManyToManyField(Person)

    class Meta:
        managed = True
        db_table = 'group'


class AddressBook(models.Model):
    persons = models.ManyToManyField(Person)
    groups = models.ManyToManyField(Group)

    class Meta:
        managed = True
        db_table = 'address_book'


class GroupMemebers(models.Model):
    group_id = models.IntegerField()
    person_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'group_group_members'
