# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
#
# from apps.sponsors.models import Sponsor
#
#
# @registry.register_document
# class SponsorDocument(Document):
#     class Index:
#         name = 'sponsor'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
#
#     class Django:
#         model = Sponsor
#
#     fields = [
#         'full_name',
#         'phone_number',
#         'type',
#         'organization',
#         'payment_amount',
#
#     ]
