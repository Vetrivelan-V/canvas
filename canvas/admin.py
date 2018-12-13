from django.contrib import admin

# Register your models here.
from canvas.models import *

admin.site.register(CanvasUser)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Announcement)
admin.site.register(Registerd)