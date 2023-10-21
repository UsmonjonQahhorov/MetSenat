from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sponsor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status



class SponsorTests(APITestCase):
    fixtures = ["sponsors.json"]
    # sponsors_url = reverse("sponsors")
    #
    # def setUp(self):

    #     self.user = User.objects.create_user(username="usmon", password="1")
    #     self.token = Token.objects.create(user=self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)
    #
    # def tearDown(self):
    #     pass
    #
    # def test_sponsor_authenticated(self):
    #     response = self.client.get(self.sponsors_url)
    #     self.assertEqual(response.status, status.HTTP_200_OK)
    #
    # def test_sponsor_list(self):
    #     expecting_data = [{
    #         "count": 4,
    #         "next": None,
    #         "previous": None,
    #         "results": [
    #             {
    #                 "id": 1,
    #                 "full_name": "Usmonjon",
    #                 "phone_number": "998787323",
    #                 "payment_amount": 100000000,
    #                 "spent_amount": 0,
    #                 "created_at": "2023-10-06T07:05:25.092000Z",
    #                 "status": "confirmed"
    #             },
    #             {
    #                 "id": 2,
    #                 "full_name": "Timur",
    #                 "phone_number": "998787323",
    #                 "payment_amount": 100000000,
    #                 "spent_amount": 0,
    #                 "created_at": "2023-10-06T07:05:25.092000Z",
    #                 "status": "confirmed"
    #             },
    #             {
    #                 "id": 3,
    #                 "full_name": "Fazlidin",
    #                 "phone_number": "998784245",
    #                 "payment_amount": 200000,
    #                 "spent_amount": 0,
    #                 "created_at": "2023-10-06T07:05:49.615000Z",
    #                 "status": "confirmed"
    #             },
    #             {
    #                 "id": 4,
    #                 "full_name": "Fazlidin",
    #                 "phone_number": "998784245",
    #                 "payment_amount": 200000,
    #                 "spent_amount": 0,
    #                 "created_at": "2023-10-06T07:23:01.564000Z",
    #                 "status": "confirmed"
    #             },
    #         ]
    #     }]
    #
    #     url = reverse("sponsors-list")
    #     print(f"expecting: {expecting_data}")
    #     response = self.client.get(path=url)
    #     print(f"response: {response.data}")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expecting_data)

    def test_sponsor_detail(self):
        expecting_data = {
            "id": 1,
            "full_name": "Usmonjon",
            "phone_number": "998787323",
            "payment_amount": 1000000,
            "organization": "pdp",
            "status": "confirmed",
            "created_at": "2023-10-06T07:05:06.674000Z"
        }
        url = reverse("sponsors-detail", kwargs={"pk": 1})
        print(f"url:{url}")
        response = self.client.get(path=url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_sponsor_update(self):
        expecting_data = {
            "id": 1,
            "full_name": "Zokir",
            "type": "legal_entity",
            "phone_number": "987654321",
            "status": "confirmed",
            "organization": "pdp",
            "payment_amount": 2345678,
            "payment_type": "cash"
        }
        data = {
            "id": 1,
            "full_name": "Zokir",
            "type": "legal_entity",
            "phone_number": "987654321",
            "status": "confirmed",
            "organization": "pdp",
            "payment_amount": 2345678,
            "payment_type": "cash"
        }
        url = reverse("sponsors-detail", kwargs={"pk": 1})
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_sponsor_partial_update(self):
        expecting_data = {
            "id": 1,
            "full_name": "string",
            "type": "legal_entity",
            "phone_number": "string",
            "status": "new",
            "organization": "string",
            "payment_amount": 92233720,
            "payment_type": "cash"
        }

        url = reverse("sponsors-detail", kwargs={"pk": 1})
        data = {
            "id": 1,
            "full_name": "string",
            "type": "legal_entity",
            "phone_number": "string",
            "status": "new",
            "organization": "string",
            "payment_amount": 92233720,
            "payment_type": "cash"
        }

        response = self.client.patch(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_sponsor_delete(self):
        url = reverse("sponsors-detail", kwargs={"pk": 1})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
