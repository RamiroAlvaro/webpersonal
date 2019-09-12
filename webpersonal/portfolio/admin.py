from django.contrib import admin
from webpersonal.portfolio.models import Project


class ProjectModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectModelAdmin)
