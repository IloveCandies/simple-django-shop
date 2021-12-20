from django.contrib import admin
from mailoperations.models import*
# Register your models here.

@admin.register(Follower)
class FolowerAdmin(admin.ModelAdmin):
    list_display = ('id','mail',)