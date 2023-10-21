from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class StudentTests(APITestCase):
    fixtures = ["studentsponsor.json"]

    def setUp(self):
        self.user = User.objects.create_user(username="usmon", password="1")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

    def tearDown(self):
        pass

    def test_student_authenticated(self):
        response = self.client.get(self.sponsors_url)
        self.assertEqual(response.status, status.HTTP_200_OK)

    def test_student_list(self):
        expecting_data = [{
            "count": 4,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "full_name": "Jorabek",
                    "type": "bachelor",
                    "institute": "textilniy",
                    "allocated_amount": 7000,
                    "contract_amount": 7000
                },
                {
                    "id": 2,
                    "full_name": "Zafar",
                    "type": "bachelor",
                    "institute": "namdu",
                    "allocated_amount": 9000,
                    "contract_amount": 9000
                },
                {
                    "id": 3,
                    "full_name": "Iroda",
                    "type": "bachelor",
                    "institute": "inha",
                    "allocated_amount": 0,
                    "contract_amount": 10000
                },
                {
                    "id": 4,
                    "full_name": "string",
                    "type": "bachelor",
                    "institute": "string",
                    "allocated_amount": 0,
                    "contract_amount": 922337
                }
            ]
        }]

        url = reverse("students-list")
        print(f"expecting: {expecting_data}")
        response = self.client.get(path=url)
        print(f"response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_student_detail(self):
        expecting_data = {
            "id": 1,
            "sponsors": [
                {
                    "id": 1,
                    "sponsor": "Timur",
                    "allocated_amount": 7000
                }
            ],
            "allocated_amount": 7000,
            "created_at": "2023-10-06T07:25:57.409369Z",
            "updated_at": "2023-10-06T07:25:57.409385Z",
            "full_name": "Abdullo",
            "phone_number": "4355675",
            "type": "bachelor",
            "institute": "xz",
            "contract_amount": 92233
        }

        url = reverse("students-detail", kwargs={"pk": 1})
        response = self.client.get(path=url)
        print(f"expecting: {expecting_data}")
        print(f"response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    #
    def test_student_update(self):
        expecting_data = {
            "id": 1,
            # "created_at": "2023-10-06T07:25:57.409369Z",
            # "updated_at": "2023-10-07T08:57:00.998999Z",
            "full_name": "Jasur",
            "phone_number": "987654321",
            "type": "bachelor",
            "institute": "tyrq",
            "contract_amount": 922337,
            "sponsors": [
                2
            ]
        }
        data = {
            "full_name": "Jasur",
            "phone_number": "987654321",
            "type": "bachelor",
            "institute": "tyrq",
            "contract_amount": 922337
        }
        url = reverse("students-detail", kwargs={"pk": 1})
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_student_partial_update(self):
        expecting_data = {
            "id": 1,
            "full_name": "Abdullo",
            "phone_number": "4355675",
            "type": "bachelor",
            "institute": "xz",
            "contract_amount": 92233,
            # "sponsors": [
            #     2
            # ]
        }

        url = reverse("students-detail", kwargs={"pk": 1})
        data = {
            "full_name": "Abdullo",
            "phone_number": "4355675",
            "type": "bachelor",
            "institute": "xz",
            "contract_amount": 92233
        }

        response = self.client.patch(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_student_delete(self):
        url = reverse("students-detail", kwargs={"pk": 1})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StudentSponsorTests(APITestCase):
    fixtures = ["studentsponsor.json"]

    def test_studentsponsor_detail(self):
        expecting_data = {
            "id": 3,
            "allocated_amount": 10000,
            "created_at": "2023-10-07T10:04:59.120190Z",
            "student": 3,
            "sponsor": 4
        }
        data = {
            "allocated_amount": 10000,
            "student": 3,
            "sponsor": 4
        }
        url = reverse("student_sponsors-list")
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)
