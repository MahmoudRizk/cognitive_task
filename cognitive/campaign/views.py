from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Count

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
    query = Campaign.objects.values('country', 'category').annotate(Count('category'))
    unique_ctrys = Campaign.objects.values('country').annotate(Count('country'))
    unique_cats = Campaign.objects.values('category').annotate(Count('category'))
    report = {}
    for cat in unique_cats:
        report[cat['category']] = []

    for q in query:
        report[q['category']].append({'country': q['country'], 'count': q['category__count']})

    # Constructing the JSON object.
    countries = [{'category': []}]
    for ctry in unique_ctrys:
        countries[0]['category'].append({'label': ctry['country']})

    dataset = []
    print(report)
    for r in report:
        tmp = {}
        tmp['seriesname'] = r
        tmp['data'] = []
        for u in unique_ctrys:
            tmp['data'].append({'value': 0})
        dataset.append(tmp)

    for idx, ctry in enumerate(countries[0]['category']):
           tmp_ctry = ctry['label']
           for d in dataset:
               for r in report:
                   if(r == d['seriesname']):
                       tmp_count = 0
                       for t in report[r]:
                           if t['country'] == tmp_ctry:
                               tmp_count = t['count']
                       d['data'][idx]['value'] = tmp_count

    data_json = {'chart': {
                    "caption": "Analysis by country and category",
                    "xaxisname": "Years",
                    "yaxisname": "Total number by category",
                    "formatnumberscale": 1,
                    "plottooltext": "<b>$dataValue</b> campaign of category <b>$seriesName</b> in $label",
                    "theme": "fusion",
                    "drawcrossline": 1
                           },
                 'categories': countries,
                 'dataset': dataset,
                 }

    column2d = FusionCharts('mscolumn2d', 'ex1', '1050', '400', 'chart-1', 'json', data_json)

    return column2d.render()
