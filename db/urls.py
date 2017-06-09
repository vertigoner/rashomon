from django.conf.urls import url
from . import views

app_name = 'db'
urlpatterns = [
    # ex: /db/
    url(r'^$', views.home, name='home'),
    # ex:/db/search/
    url(r'^search/?$', views.search, name='search'),
]