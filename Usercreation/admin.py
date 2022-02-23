from django.contrib import admin
from .models import Campaigns, Organization, Users
@admin.register(Users)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["password"]

admin.site.register(Organization)
admin.site.register(Campaigns)
