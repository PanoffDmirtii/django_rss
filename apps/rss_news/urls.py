from django.conf.urls import url
from apps.rss_news import views

urlpatterns = [
    url(r'^index$', views.index)
]
