from django.contrib import admin
from .models import Colour, Material, Yarn, Pattern, User, ProjectYarn, Project

@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ('brand', 'weight', 'colour', 'material', 'price', 'yardage', 'hook_size', 'available')
    list_filter = ('colour', 'material', 'available')
    search_fields = ('brand', 'colour', 'material')

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('title', ' description', 'published', 'link', 'transcript')
    search_fields = ('title', 'description')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(ProjectYarn)
class ProjectYarnAdmin(admin.ModelAdmin):
    list_display = ('project', 'yarn', 'quantity')
    search_fields = ('project__title', 'yarn__brand')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'yarn', 'pattern', 'user', 'date_started', 'date_finished', 'notes')
    list_filter = ('date_started', 'date_finished')
    search_fields = ('title', 'description', 'user__username')

admin.site.register(Colour)
admin.site.register(Material)
