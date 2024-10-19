from django.contrib import admin

from urlsAndViews.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
