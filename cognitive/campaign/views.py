from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from campaign.models import Campaign
from campaign.forms import CampaignForm


def campaign(request):
    return render(request, "pages/campaign.html")


class CampaignFormView(FormView):
    form_class = CampaignForm
    template_name = "pages/campaign_form.html"
    success_url = reverse_lazy("campaign:campaign")

    def form_valid(self, form):
        form.save()
        return super(CampaignFormView, self).form_valid(form)


class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaign_list'
    template_name = "pages/campaign.html"
