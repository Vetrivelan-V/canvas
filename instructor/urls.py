
from django.conf.urls import url
from . import views

app_name = 'instructor'
urlpatterns = [
    url(r'^$', views.index, name='login_func'),
    url(r'^instructor/$', views.instructorlogin, name='instructorlogin'),

]