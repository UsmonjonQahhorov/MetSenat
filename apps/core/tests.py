# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
#
#
# class DashboardAPITestCase(APITestCase):
#
#
#     def test_chart_one(self):
#         url = reverse("dashboard_one-list")
#
#         expected_data = {
#             "total_allocated_amount": 16000,
#             "total_contract_amount": 948337,
#             "left_contract_amount": 932337
#         }
#
#         response = self.client.get(path=url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, expected_data)
#
# def test_chart_two(self):
#     response = self.client.get('dashboards-list')
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     expected_data = {
#         "students": {
#             "2023-10-07": 10,
#
#         },
#         "sponsors": {
#             "2023-10-07": 5,
#
#         },
#     }
#
#     self.assertEqual(response.data, expected_data)
