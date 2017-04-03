from django.conf.urls import url
from . import views

urlpatterns = [

            url(r'^$', views.home),
            url(r'^results/(?P<query_id>[a-zA-Z0-9]{6})', views.search_results, name = 'search_results'),

        ]
