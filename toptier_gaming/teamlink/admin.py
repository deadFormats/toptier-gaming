from django.contrib import admin
from .models import TeamPost

# Register your models here.
@admin.register(TeamPost)
class TeamPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'visibility']
    list_filter = ['status', 'visibility', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']   
