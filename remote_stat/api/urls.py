from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('add', views.AddAPIView.as_view()),
    path('average', views.AverageAPIView.as_view()),
    path('mean', views.MeanAPIView.as_view()),
    path('statistics', views.StatisticsAPIView.as_view()),
    path('clear', views.ClearAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
