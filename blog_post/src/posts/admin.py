from django.contrib import admin
from .models import PostModel, Profile

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Profile)
