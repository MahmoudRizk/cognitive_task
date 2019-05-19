from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse

from campaign.models import Campaign
from campaign.forms import CampaignForm
from .fusioncharts import FusionCharts


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
    paginate_by = 5
    queryset = Campaign.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output'] = chart()
        return context


def chart():
    column2d = FusionCharts('mscolumn2d', 'ex1', '1050', '400', 'chart-1', 'json', """{
      "chart": {
        "caption": "Analysis by country and category",
        "xaxisname": "Years",
        "yaxisname": "Total number by category",
        "formatnumberscale": "1",
        "plottooltext": "<b>$dataValue</b> campaign of category <b>$seriesName</b> in $label",
        "theme": "fusion",
        "drawcrossline": "1"
      },
      "categories": [
        {
          "category": [
            {
              "label": "EGY"
            },
            {
              "label": "USA"
            },
            {
              "label": "KSA"
            },
            {
              "label": "RU"
            },
            {
              "label": "GB"
            }
          ]
        }
      ],
      "dataset": [
        {
          "seriesname": "Sports",
          "data": [
            {
              "value": "125"
            },
            {
              "value": "300"
            },
            {
              "value": "480"
            },
            {
              "value": "800"
            },
            {
              "value": "110"
            }
          ]
        },
        {
          "seriesname": "Tecgnology",
          "data": [
            {
              "value": "700"
            },
            {
              "value": "150"
            },
            {
              "value": "350"
            },
            {
              "value": "600"
            },
            {
              "value": "140"
            }
          ]
        },
        {
          "seriesname": "Automotive",
          "data": [
            {
              "value": "100"
            },
            {
              "value": "100"
            },
            {
              "value": "300"
            },
            {
              "value": "600"
            },
            {
              "value": "900"
            }
          ]
        }
      ]
    }""")

    return column2d.render()
    # return render(request, 'pages/campaign.html', {'output': column2d.render()})
