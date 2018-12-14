import os
from datetime import datetime

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render

from canvas.forms import LoginForm
#
# def hello(request,number):
#     text = "<h1>welcome to my app %s !</h1>"% number
#     return HttpResponse(text)
#
# # Create your views here.
from canvas.models import Course, Announcement, Assignment, CanvasUser, Registerd


def home_func(request):
    if request.method == "POST":
        # Get the posted form

        studentLogin = LoginForm(request.POST)

        if studentLogin.is_valid():
            try:
                username = studentLogin.clean_message()
                print(username)
                if username.user_type == 1:
                    course = Course.objects.filter(user=username.ub_id)
                else:
                    reg = Registerd.objects.filter(student=username.ub_id)
                    course = list()
                    for items in reg:
                        course.append(items.course_id)

                response = render(request, 'home_page.html',
                                  {"userinfo": username, "lastlogin": username.last_login, "course": course})
                response.set_cookie('last_connection', datetime.now())
                response.set_cookie('ub_id', username.ub_id)
                response.set_cookie('user_type', username.user_type)
                return response

            except forms.ValidationError as e:
                return render(request, "login.html", {"error_message": e.message})


def login_func(request):
    return render(request, "login.html", {})


def coursedetails_func(request, number):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    print(ub_id)
    if int(number) > 0:
        print("Edit Details")
        course = Course.objects.get(pk=int(number))

        response = render(request, 'course_details.html', {"course": course, "ub_id": ub_id, "user_type": user_type})
        response.set_cookie('course_id', course.course_id)
        return response
    else:
        print("Add Details")
        return render(request, 'course_details.html', {"ub_id": ub_id, "user_type": user_type})


def announcements_func(request):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    course_id = request.COOKIES.get('course_id')
    listofAnnoucement = Announcement.objects.filter(course=course_id)
    print(listofAnnoucement)
    return render(request, 'announcementlist.html', {"listofAnnoucement": listofAnnoucement})


def people(request):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    course_id = request.COOKIES.get('course_id')
    listofStudent = Course.objects.get(pk=course_id)
    listofStudent.students
    return render(request, 'peoplelist.html', {"listofStudent": listofStudent.students.all()})


def addUpdateCourse(request):
    return render(request, "addcourse.html", {})


def assignments_func(request, type):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    course_id = request.COOKIES.get('course_id')
    if user_type==1:
        #Admin
        listOfAssignments = Assignment.objects.filter(course=course_id, user=ub_id, type=type)
    else:
        #Student
        admin_id=Course.objects.get(pk=course_id)
        listOfAssignments = Assignment.objects.filter(course=course_id,user__in=(ub_id,admin_id.user.ub_id) , type=type)


    return render(request, 'assignment_upload.html', {"listOfAssignments": listOfAssignments, "type": type,"user_type": user_type})

def grades(request):
    ub_id = request.COOKIES.get('ub_id')
    user_type = request.COOKIES.get('user_type')
    course_id = request.COOKIES.get('course_id')
    listOfAssignments = Assignment.objects.filter(course=course_id,user__in=(ub_id) , type=1)
    return render(request, 'gradelist.html', {"listOfAssignments": listOfAssignments, "type": type,"user_type": user_type})


def assignment_add(request):
    folder = request.path.replace("/", "_")
    uploaded_filename = request.FILES['file'].name
    dirpath = "/var/www/html/canvas/"
    course_id = request.COOKIES.get('course_id')
    ub_id = request.COOKIES.get('ub_id')
    dirpath
    folderPath = course_id + '/' + ub_id + "/"
    type = request.POST.get('type')
    parent_id=request.POST.get('parent_id')
    # create the folder if it doesn't exist.
    try:
        os.mkdir(os.path.join(dirpath, course_id))
    except:
        pass
    try:
        os.mkdir(os.path.join(dirpath, course_id + "/" + ub_id))
    except:
        pass
    # save the uploaded file inside that folder.
    full_filename = os.path.join("/var/www/html/canvas/", folderPath, uploaded_filename)
    fout = open(full_filename, 'wb+')
    # Iterate through the chunks.
    try:
        for chunk in request.FILES['file'].file:
            fout.write(chunk)
        fout.close()
    except:
        html = "<html><body>NOT SAVED</body></html>"
        return HttpResponse(html)
    canvas_user = CanvasUser.objects.get(pk=ub_id)
    course = Course.objects.get(pk=course_id)
    if parent_id:
        parent=Assignment.objects.get(pk=parent_id)
        assignment = Assignment.objects.create(file_only_name=uploaded_filename,
                                           file_name="http://localhost/canvas/" + folderPath + uploaded_filename,
                                           type=type, user=canvas_user, course=course, parent_Id=parent)
    else:
        assignment = Assignment.objects.create(file_only_name=uploaded_filename,
                                               file_name="http://localhost/canvas/" + folderPath + uploaded_filename,
                                               type=type, user=canvas_user, course=course)
    html = "<html><body>SAVED</body></html>"
    return HttpResponse(html)
