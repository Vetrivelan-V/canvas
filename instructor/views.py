from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from .forms import InstructorForm
from .models import Instructor

def index(request):
    return render(request, 'instructor/instructorlogin.html', {})



def instructorlogin(request):

    if request.method == 'POST':
        instructorLoginForm = InstructorForm(request.POST)

        if instructorLoginForm.is_valid():
            instructoremailid = instructorLoginForm.cleaned_data['emailid']
            instructorpassword = instructorLoginForm.cleaned_data['password']
            qs = Instructor.objects.filter(emailid=instructoremailid)
            if qs.password == instructorpassword:
                return render(request, 'instructorhomepagehtml', {"instructorinfo": qs})



        with connection.cursor() as cursor:
            cursor.execute("select password from Instructor where emailid = %s", emailid)
            row = cursor.fetchone()
            if( password == row[0].password):
                return redirect("instructor/homepage.html")

        # else:
        #     print("Someone tried to login and failed.")
        #     print("They used username: {} and password: {}".format(username,password))
        #     return HttpResponse("Invalid login details given")
    else:
        return render(request, 'instructor/instructorlogin.html', locals())
