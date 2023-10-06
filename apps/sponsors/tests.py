from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# from .models import Sponsor


class SponsorTests(APITestCase):
    # def test_sponsor_list(self):
    #     expecting_data = [
    #         {
    #             "id": 1,
    #             "name": "P12",
    #         },
    #         {
    #             "id": 2,
    #             "name": "P13",
    #         },
    #     ]
    #     url = reverse("sponsor-list")
    #     response = self.client.get(path=url)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expecting_data)
    #
    # def test_sponsor_create(self):
    #     expecting_data = {
    #         "id": 1,
    #         "fullname": "Qohhorov Usmonjon"
    #     }
    #     url = reverse("sponsor-list")
    #     data = {
    #         "name": ""
    #     }
    #     response = self.client.post(path=url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data, expecting_data)

    def test_sponsor_detail(self):
        expecting_data = {
            "id": 2,
            "fullname": "Usmonjon Qohhorov",
            "payment_amount": 12345.0,
            "phone_number": "+998997654321",
            "name_comp": "Wilsacom",
            "is_staff": False,
            "spend_amount": 132.0,
            "sponsor_status": "jismoniy shaxs",
            "sponsorship_status": "yangi"
        }
        url = reverse("sponsor-detail", kwargs={"pk": 2})
        response = self.client.get(path=url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)
    #
    # def test_sponsor_update(self):
    #     group_name = "P15"
    #     expecting_data = {
    #         "id": 2,
    #         "name": group_name
    #     }
    #     url = reverse("sponsor-detail", kwargs={"pk": 2})
    #     data = {
    #         "name": group_name
    #     }
    #     response = self.client.put(path=url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expecting_data)
    #
    # def test_sponsor_partial_update(self):
    #     group_name = "P15"
    #     expecting_data = {
    #         "id": 2,
    #         "name": group_name
    #     }
    #     url = reverse("sponsor-detail", kwargs={"pk": 2})
    #     data = {
    #         "name": group_name
    #     }
    #     response = self.client.patch(path=url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expecting_data)
    #
    # def test_sponsor_delete(self):
    #     url = reverse("sponsor-detail", kwargs={"pk": 2})
    #     response = self.client.delete(path=url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)