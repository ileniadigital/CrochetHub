from django.contrib import admin
from .models import Colour, Material, Yarn, Pattern, User, Project, PatternYarn

@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ('brand', 'colour', 'material', 'weight', 'price', 'yardage', 'hook_size')
    search_fields = ('brand', 'colour', 'material')

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'link')
    search_fields = ('title',)
    list_filter = ('published',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_started', 'finished', 'date_finished')
    search_fields = ('title', 'user__username')
    list_filter = ('finished', 'date_started', 'date_finished')

@admin.register(PatternYarn)
class PatternYarnAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'yarn', 'quantity')
    search_fields = ('pattern__title', 'yarn__brand')
