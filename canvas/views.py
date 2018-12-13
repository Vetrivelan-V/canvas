from datetime import datetime

from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse

from canvas.forms import LoginForm

#
# def hello(request,number):
#     text = "<h1>welcome to my app %s !</h1>"% number
#     return HttpResponse(text)
#
# # Create your views here.
from canvas.models import Course, Announcement


def main(request):
    if request.method == "POST":
        # Get the posted form
        studentLogin = LoginForm(request.POST)
        value=0
        if studentLogin.is_valid():
            try:
                username = studentLogin.clean_message()
                print(username)
            except forms.ValidationError:
                value=-1
        else:
            value=-1
        if value==0:
            course=Course.objects.filter(user=username.ub_id)
            response =render(request, 'Main.html', {"userinfo": username,"lastlogin":username.last_login,"course":course})
            response.set_cookie('last_connection', datetime.now())
            response.set_cookie('ub_id', username.ub_id)
            response.set_cookie('user_type', username.user_type)
            return response
        else:

            return  render(request,"index.html",{})
#
# def date(request):
#     today = datetime.datetime.now().date()
#     return render(request, "date.html", {"today": today})

def index(request):
    return render(request,"index.html",{})

def details(request,number):
    ub_id=request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    print(ub_id)
    if int(number) >0:
        print("Edit Details")
        course=Course.objects.get(pk=int(number))

        response=render(request, 'details.html', {"course": course,"ub_id" :ub_id,"user_type":user_type})
        response.set_cookie('course_id', course.course_id)
        return response
    else:
        print("Add Details")
        return render(request, 'details.html', {"ub_id": ub_id, "user_type": user_type})

def announcements(request):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    course_id = request.COOKIES.get('course_id')
    listofAnnoucement=Announcement.objects.filter(course=course_id)
    print(listofAnnoucement)
    return render(request, 'details.html', {"listofAnnoucement": listofAnnoucement})



def addUpdateCourse(request):
    return render(request,"addcourse.html",{})