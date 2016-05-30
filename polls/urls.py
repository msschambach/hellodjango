from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='polls_index'),
    url(r'^create', views.create_poll, name='create_poll'),
    url(r'^save', views.save_poll, name='save_poll'),
    url(r'^(?P<question_id>[0-9]+)/$',views.single_poll_vote, name='single_poll_vote'),
    url(r'^(?P<question_id>[0-9]+)/vote',views.single_poll_save_vote, name='single_poll_save_vote'),
    url(r'^(?P<question_id>[0-9]+)/results',views.single_poll, name='single_poll'),
]
