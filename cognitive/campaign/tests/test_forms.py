from django.test import TestCase
from django.urls import reverse_lazy

from campaign.models import Campaign
from campaign.forms import CampaignForm


class CampaignFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        global valid_data
        global invalid_data
        valid_data = {
               'name': 'n99',
               'country': 'EGY',
               'budget': '199',
               'goal': 'Awareness',
               'category': 'Sports'
               }

        invalid_data = {
               'name': '',
               'country': '',
               'budget': '',
               'goal': '',
               'category': ''
              }

    def test_campaignForm_valid(self):
        form = CampaignForm(valid_data)
        self.assertTrue(form.is_valid())

    def test_campaignForm_invalid(self):
        form = CampaignForm(invalid_data)
        self.assertFalse(form.is_valid())
