from django.conf.urls import  url
from . import views

app_name='canvas'

urlpatterns = [
    url(r'^$', views.login_func, name='login_func'),
    url(r'^home_func/$', views.home_func, name='home_func'),
    url(r'^coursedetails_func/(\d+)/$', views.coursedetails_func, name='coursedetails_func'),
    url(r'^announcements_func/$', views.announcements_func, name='announcements_func'),
    url(r'^assignments_func/(\d+)/$', views.assignments_func, name='assignments_func'),
    url(r'^assignment_add/$', views.assignment_add, name='assignment_add'),
    url(r'^addUpdateCourse/$', views.addUpdateCourse, name='addUpdateCourse'),
    url(r'^people/$', views.people, name='people'),
    url(r'^grades/$', views.grades, name='grades'),

    #url('hello/(\d+)', views.hello, name='hello'),

]


