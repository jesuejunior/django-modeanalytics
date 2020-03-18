import base64
import hashlib
import hmac
import time
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models


def f():
    return {"max_age": 1800}


class ModeReportModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Report Name")
    run_token = models.CharField(max_length=16, verbose_name="Run Token")
    space = models.CharField(max_length=16, blank=True, null=True, verbose_name="Space")
    params = JSONField(default=f, verbose_name="Query Parameters(JSON)", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "report"
        verbose_name = "Report"
        ordering = ("pk",)

    def __create_url(self, timestamp: int) -> str:
        org: str = settings.MODE_ORG
        access_key: str = settings.MODE_ACCESS_KEY
        self.params.update({"timestamp": timestamp})
        query: str = urlencode(sorted(self.params.items()), doseq=True, encoding="utf-8")
        return f"https://app.mode.com/{org}/reports/{self.run_token}/embed?access_key={access_key}&{query}"

    def sign_url(self) -> str:
        """
            Generates https://app.mode.com/octan/reports/0d57a7jr4789/embed?access_key=1231794bgrb3&param_sales_region=North%20America&timestamp=1532446786,1532446786
        """
        secret: str = settings.MODE_ACCESS_SECRET
        timestamp: int = int(time.time())
        url: str = self.__create_url(timestamp)

        request_type: str = "GET"
        content_type: str = ""  # FIXME: remove it
        content_body: str = ""  # FIXME: remove it
        content_hash: str = hashlib.md5(content_body.encode()).digest()
        content_digest: str = base64.encodestring(content_hash).strip().decode()

        request_string: str = ",".join([request_type, content_type, content_digest, url, str(timestamp)])
        signature = hmac.new(secret.encode(), msg=request_string.encode(), digestmod=hashlib.sha256).hexdigest()
        signed_url: str = f"{url}&signature={signature}"
        return signed_url
