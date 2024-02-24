from django.contrib import admin

# Register your models here.
# interview/admin.py
from django.contrib import admin
from .models import InterviewQuestion

admin.site.register(InterviewQuestion)
