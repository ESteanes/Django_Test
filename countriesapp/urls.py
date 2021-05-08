from django.conf.urls import url
from countriesapp import views


urlpatterns = [
    url(r'^api/countriesapp$',views.countries_list),
    url(r'api/countriesapp/(?P<pk>[0-9]+)$',views.countries_detail)
]