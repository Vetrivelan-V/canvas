
from django.conf.urls import url
from . import views

app_name = 'instructor'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^instructor/$', views.instructorlogin, name='instructorlogin'),

]