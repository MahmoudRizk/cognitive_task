from django.urls import path

from . import views
app_name = "campaign"

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaign'),
    path('add/', views.CampaignFormView.as_view(), name='campaign_form'),
]
