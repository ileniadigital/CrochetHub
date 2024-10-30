from django.contrib import admin
from .models import Yarn, Pattern, User, PatternYarn, Project

@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ('id','brand', 'weight', 'colour', 'material', 'price', 'yardage', 'hook_size')
    search_fields = ('brand', 'colour', 'material')

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'link', 'transcript')
    search_fields = ('title',)
    list_filter = ('published',)
    date_hierarchy = 'published'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(PatternYarn)
class PatternYarnAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'yarn', 'quantity')
    search_fields = ('pattern__title', 'yarn__brand')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'pattern', 'user', 'date_started', 'finished', 'date_finished')
    search_fields = ('title', 'pattern__title', 'user__username')
    list_filter = ('finished', 'date_started', 'date_finished')
    date_hierarchy = 'date_started'