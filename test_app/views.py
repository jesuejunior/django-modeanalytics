from django.template.response import TemplateResponse
from django.views.generic import View

from .models import AppReportModel


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        url: str = AppReportModel.objects.get(pk=1).sign_url()
        return TemplateResponse(request=self.request, template=self.template_name, context={"url": url}, **kwargs)
