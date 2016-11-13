"""
Controller for the REST API. This will accept requests and give response as JSON.

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ginger_address_book.services.address_book_service import AddressBookService


class PersonView(APIView):
    """ This view deals with the Person """

    def post(self, request, format=None):
        try:
            person_id = AddressBookService().add_person_to_address_book(request.data)
            return Response(status=status.HTTP_201_CREATED, data=person_id)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})

    def get(self, request, id, format=None):
        try:
            person_dict = AddressBookService().get_person_details_by_id(id)
            return Response(status=status.HTTP_200_OK, data=person_dict)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})


class GroupView(APIView):
    """ This view deals with the Group """

    def post(self, request, format=None):
        try:
            group_id = AddressBookService().add_group_to_address_book(request.data)
            return Response(status=status.HTTP_200_OK, data=group_id)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})

    def get(self, request, id, format=None):
        try:
            group_dict = AddressBookService().get_group_details_by_id(id)
            return Response(status=status.HTTP_200_OK, data=group_dict)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})

    def put(self, request, id, format=None):
        try:
            AddressBookService().add_members_to_group(id, request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})


class PersonGroupDetails(APIView):
    """ This view deals with the group details of a person """

    def get(self, request, id, format=None):
        try:
            detail_list = AddressBookService().find_group_by_members(id)
            return Response(status=status.HTTP_200_OK, data=detail_list)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})


class SearchView(APIView):
    """ This view deals with the Search functionality """

    def get(self, request, format=None):
        try:
            search_str = request.GET['query']
            search_result = AddressBookService().find_person_by_name(search_str)
            return Response(status=status.HTTP_200_OK, data=search_result)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": str(e)})
