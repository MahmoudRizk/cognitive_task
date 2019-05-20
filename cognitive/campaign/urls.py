from django.urls import path

from . import views

app_name = "campaign"

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaign'),
    path('add/', views.CampaignFormView.as_view(), name='campaign_form'),
    path('api/', views.CampaignViewSet.as_view({'get': 'list'}), name='campaign_api'),
    path('api/<int:pk>/', views.CampaignDetailSet.as_view()),
    path('api/create/', views.CampaignCreate.as_view()),
]
