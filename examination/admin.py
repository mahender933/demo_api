from django.contrib import admin
from .models import Exam, Subject, SubCategory, Topic

# Register your models here.
admin.site.register([Exam, Subject, SubCategory, Topic])

