from django.test import TestCase
from django.urls import reverse_lazy

from campaign.models import Campaign

class CampaignFormViewTest(TestCase):
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

    def test_formView_valid_add_campaign(self):
        response = self.client.post(reverse_lazy('campaign:campaign_form'), valid_data)
        self.assertEqual(response.status_code, 302)

    def test_formView_invalid_add_campaign(self):
        response = self.client.post(reverse_lazy('campaign:campaign_form'), invalid_data)
        self.assertEqual(response.status_code, 200)


class CampaignListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 campaigns for pagination tests
        number_of_campaigns = 13

        for campaign_id in range(number_of_campaigns):
            Campaign.objects.create(
                name='n'+str(campaign_id),
                country='USA'+str(campaign_id),
                budget=199,
                goal='Awareness',
                category='Sports'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/campaign/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('campaign:campaign'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy('campaign:campaign'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/campaign.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse_lazy('campaign:campaign'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['campaign_list']) == 5)

    def test_lists_all_campaigns(self):
        # Get third page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse_lazy('campaign:campaign')+'?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['campaign_list']) == 3)
