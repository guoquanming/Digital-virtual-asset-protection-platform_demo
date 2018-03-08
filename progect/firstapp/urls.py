from django.conf.urls import url

from firstapp import search
from . import views
from firstapp import owner_b,hacker

urlpatterns = [
    url(r'^$', views.display_list),
    url(r'^add/$', search.add),
    url(r'^owner_b.html/$', owner_b.display_message),
    url(r'^hacker.html/$', hacker.hacker_display),
]


