# Address Book

## Problem Statement:
https://github.com/gingerpayments/hiring/blob/master/coding-assignments/python-address-book-assignment/python-address-book-assignment.rst

## Technologies Used:
1. Python 2.7
2. Django
3. Django Rest Framework

## How To Run:
1. Clone the repository
2. cd ginger_address_book
3. Go to your virtual env
4. pip install -r requirements.txt
5. python manage.py syncdb
6. python manage.py migrate
7. python manage.py runserver
8. Sever will be running in 127.0.0.1:8000 by default

## Project Structure
1. urls.py : Holds the endpoints to the views
2. views: Accept the request from the client and passes it to the services, also returns the serialized response to the client.
3. services: Services holds the business logic.
4. models: They do the database transactions
5. serializers: Helps in serialize the data from database.
6. tests: Unit test for the project

## Design Question
Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an email address in the address book) - discuss how you would implement this without coding the solution.

Simple way: As we are already keeping the email address in our database, we can do a LIKE query to retrieve the same. This is the same way we have already implemented the name based search.

SELECT * FROM email WHERE email_str LIKE '%com%' ;

Longterm Solution: Search's are always supposed to be fast.  When we entirely rely search on the database is not a safe idea.  Because, as the data increases the search will get slow.  Indexing the data required to be searched is the solution.  There is a deal of convenient way to achieve that, like Solr search.  By this when we create a new data or update we will pass this to our Solr node also, and all searches will be performed against this. Also we can use Amazon Cloud Search or Elastic Search for the purpose. This will spare us from the node handling effort.

## Api Document:

**Add a person to the address book:**

url: 127.0.0.1:8000/person/

type: POST

request: {
  "first_name": "Najeeb",
  "last_name": "T",
  "address": [
    "K R puram",
    "Bangalore "
  ],
  "phone": [
    "919447723553",
    "919876543210"
  ],
  "email": [
    "najeeb.1989@gmail.com"
    ]
}
response: person_id (integer)

**Add a group to the address book:**

url: 127.0.0.1:8000/group/

type: POST

request: {
  "group_name": "new group"
}
response: group_id (integer)

**Add person/s to a group in the address book:**

url: 127.0.0.1:8000/group/{group_id}

type: PUT

request: {
  "add_list": [1] // list of person id's
}

**Given a group we want to easily find its members:**

url: 127.0.0.1:8000/group/{group_id}

type: GET

response: {
  "group_members": [
    {
      "first_name": "Najeeb",
      "last_name": "T",
      "id": 1
    }
  ],
  "group_name": "friends"
}

**Given a person we want to easily find the groups the person belongs to:**
url: 127.0.0.1:8000/person_group_details/{person_id}

type: GET

response:
[
  {
    "group_name": "friends",
    "group_members": [
      1,
      9
    ]
  },
  {
    "group_name": "family",
    "group_members": [
      9,
      10
    ]
  }
]

**Find person by name (can supply either first name, last name, or both):**
url: 127.0.0.1:8000/search?query={user input}

type: GET

response: [
  {
    "first_name": "Najeeb",
    "last_name": "T",
    "addresses": [],
    "email_addresses": [],
    "phone_numbers": []
  },
  
  {
    "first_name": "Nabeel",
    "last_name": "T",
    "addresses": [
      15,
      16
    ],
    "email_addresses": [
      5,
      6
    ],
    "phone_numbers": [
      3,
      4
    ]
  }
]




