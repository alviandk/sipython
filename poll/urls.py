from django.conf.urls import url

from . import views

urlpatterns = [
    # /poll/
    url(r'^$', views.index, name='index'),
    # /poll/help/
    url(r'^help/$', views.help, name='help'),
]
