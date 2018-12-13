from django.conf.urls import  url
from . import views

app_name='canvas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^details/(\d+)/$', views.details, name='details'),
    url(r'^announcements/$', views.announcements, name='announcements'),
    url(r'^addUpdateCourse/$', views.addUpdateCourse, name='addUpdateCourse'),

    #url('hello/(\d+)', views.hello, name='hello'),

]


