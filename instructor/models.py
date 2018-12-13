from django.db import models


class Course(models.Model):
    courseid = models.CharField(max_length=20,primary_key=True)
    coursename = models.CharField(max_length=50)

    def __str__(self):
        return self.courseid+" "+self.coursename

    class Meta:
        db_table = 'Course'

class Instructor(models.Model):
    name = models.CharField(max_length=20)
    emailid = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    courseid = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" "+self.courseid

    class Meta:
        db_table = 'Instructor'



