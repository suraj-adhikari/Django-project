from django.contrib import admin

from town import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
