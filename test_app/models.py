from django.db import models

from modeanalytics.models import ModeReportModel


class AppReportModel(ModeReportModel):
    app_name = models.CharField(max_length=10)

    class Meta:
        db_table = "app_report"
        verbose_name = "App Reports"
