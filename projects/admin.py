from django.contrib import admin
from .models import Project,Review,Tag
#used to show classes from models.py in admin pannel


admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
