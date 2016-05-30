from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='polls_api_index'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='polls_api_question_detail'),
    url(r'^choice/(?P<pk>[0-9]+)/$', views.ChoiceDetail.as_view(), name='polls_api_choice_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
