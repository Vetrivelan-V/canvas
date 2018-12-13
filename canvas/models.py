from django.db import models

# Create your models here.
class CanvasUser(models.Model):
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    ub_id=models.AutoField(primary_key=True)
    email_id=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    user_type=models.IntegerField()
    create_date=models.DateTimeField(auto_now_add=True,blank=True)
    last_login=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return ""+self.email_id + " | "+ self.first_name +"_"+self.last_name

    class Meta:
        ordering = ('create_date',)



class Course(models.Model):
    course_name= models.CharField(max_length=30)
    course_id = models.AutoField(primary_key=True)
    create_date=models.DateTimeField(auto_now_add=True,blank=True)
    user = models.ForeignKey(CanvasUser, on_delete=models.CASCADE, related_name='professor')
    students=models.ManyToManyField(CanvasUser,through="Registerd", related_name='students')
    def __str__(self):
        return str(self.course_id)+" | "+ self.course_name
    class Meta:
        ordering = ('create_date',)

class Registerd(models.Model):
    registerd = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    student=models.ForeignKey(CanvasUser,on_delete=models.CASCADE)
    def __str__(self):
        return  str(self.registerd)+" | "+str(self.course_id)+" | "+str(self.student)
class Assignment(models.Model):
    file_name=models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    assignment_id=models.AutoField(primary_key=True)
    grade=models.CharField(max_length=1)
    type=models.IntegerField(default=1)
    submissionDate=models.DateTimeField(auto_now_add=True,blank=True)
    user = models.ForeignKey(CanvasUser, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.assignment_id)+" | "+str(self.create_date)
    class Meta:
        ordering = ('create_date',)


class Announcement(models.Model):
    announcement_details=models.TextField()
    announcement_id=models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(CanvasUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.announcement_id)+" | "+str(self.create_date)
    class Meta:
        ordering = ('create_date',)


