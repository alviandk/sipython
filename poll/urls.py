from django.conf.urls import url

from . import views

urlpatterns = [
    # /poll/
    url(r'^$', views.index, name='index'),
    # /poll/help/
    url(r'^help/$', views.help, name='help'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$',
        views.detail_question, name='detail_question'),
    # /poll/help/
    url(r'^vote/$', views.vote, name='vote'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$',
        views.results, name='results'),
]
