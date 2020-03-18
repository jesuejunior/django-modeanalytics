from typing import Dict

from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .models import AppReportModel


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        report_id = 2
        params: Dict[str, str] = request.GET.dict()
        url: str = AppReportModel.objects.get(pk=report_id).get_report_url(params)
        return TemplateResponse(request=self.request, template=self.template_name, context={"url": url}, **kwargs)
