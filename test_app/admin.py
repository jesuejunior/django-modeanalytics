from django.contrib import admin

from .models import AppReportModel


class AppReportAdmin(admin.ModelAdmin):
    pass


admin.site.register(AppReportModel, AppReportAdmin)
