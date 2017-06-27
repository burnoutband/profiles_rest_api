from django.contrib import admin

# from profiles_api import models
from . import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)

