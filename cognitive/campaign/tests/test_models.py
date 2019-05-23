from django.test import TestCase
from django.urls import reverse_lazy

from campaign.models import Campaign


class CampaignModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        global campaign
        campaign = Campaign.objects.create(
                        name='n1',
                        country='USA',
                        budget=199,
                        goal='Awareness',
                        category='Sports'
                    )

    def test_name_max_length(self):
        max_length = campaign._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_country_max_length(self):
        max_length = campaign._meta.get_field('country').max_length
        self.assertEquals(max_length, 50)

    def test_goal_max_length(self):
        max_length = campaign._meta.get_field('goal').max_length
        self.assertEquals(max_length, 50)

    def test_category_max_length(self):
        max_length = campaign._meta.get_field('category').max_length
        self.assertEquals(max_length, 50)

    def test_campaign_str(self):
        self.assertEqual(campaign.__str__(), campaign.name)
