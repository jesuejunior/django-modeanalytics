from typing import Dict

from django.conf import settings
from django.test import TestCase

from .models import ModeReportModel


class TestGenerateReportUrl(TestCase):
    """
    How to validate using a mode tool
    Link: https://mode.com/help/articles/test-your-white-label-embeds/
    """

    settings.MODE_ORG = "test"
    settings.MODE_ACCESS_KEY = "1234567890"
    settings.MODE_ACCESS_SECRET = "0987654321"

    def test_create_url_ok(self):
        ts: int = 1_532_446_786
        expected = "https://app.mode.com/test/reports/12eaf1245c7e/embed?access_key=1234567890&max_age=1800&timestamp=1532446786"
        model = ModeReportModel()
        model.name = "test1"
        model.run_token = "12eaf1245c7e"

        result: str = model._ModeReportModel__create_url(ts)
        self.assertEqual(expected, result)

    def test_sign_url_ok(self):

        ts: int = 1_532_446_786
        url = "https://app.mode.com/test/reports/12eaf1245c7e/embed?access_key=1234567890&max_age=1800&timestamp=1532446786"
        model = ModeReportModel()
        model.name = "test1"
        model.run_token = "12eaf1245c7e"

        result: str = model._ModeReportModel__sign_url(url, ts)
        expected: str = "https://app.mode.com/test/reports/12eaf1245c7e/embed?access_key=1234567890&max_age=1800&timestamp=1532446786&signature=bce6321f616c77321e8dcc7943b6f3f8c23425b23c87a14a23395a423f605da9"
        self.assertEqual(expected, result)

    def test_params_ok(self):
        model = ModeReportModel()
        model.name = "testx"
        model.run_token = "12eaf1245c7e"
        params: Dict[str, str] = {"email": "jj@admin.com"}
        model._ModeReportModel__convert_params(params)

        expected: Dict[str, str] = {"max_age": 1800, "param_email": "jj@admin.com"}
        self.assertEqual(expected, model.params)

    def test_params_error(self):
        model = ModeReportModel()
        model.name = "testy"
        model.run_token = "12eaf1245c7e"
        params: Dict[str, str] = {"email": "jj@admin"}
        model._ModeReportModel__convert_params(params)

        expected: Dict[str, str] = {"max_age": 1800, "email": "jj@admin"}
        self.assertNotEqual(expected, model.params)

    def test_params_override(self):
        model = ModeReportModel()
        model.name = "testy"
        model.run_token = "12eaf1245c7e"
        model.params.update({"display[]": "right_side"})
        params: Dict[str, str] = {"email": "jj@admin", "display[]": "left_side"}

        model._ModeReportModel__convert_params(params)

        expected: Dict[str, str] = {"max_age": 1800, "param_email": "jj@admin", "param_display[]": "left_side"}
        self.assertEqual(expected, model.params)

    def test_params_saved_override(self):
        model = ModeReportModel()
        model.id = 1
        model.name = "testy"
        model.run_token = "12eaf1245c7e"
        model.params.update({"email": ""})
        model.save()
        params: Dict[str, str] = {"email": "x@x.com", "phone": ""}
        
        report = ModeReportModel.objects.get(pk=1)
        report._ModeReportModel__convert_params(params)
        expected: Dict[str, str] = {"max_age": 1800, "param_email": "x@x.com", "param_phone": ""}
        self.assertEqual(expected, report.params)
    
    def test_mixed_params(self):
        """
        Test when there are params from web and from db with same names
        emails[] -> db
        emails -> web
        """
        pass

    def test_get_full_report_url(self):
        """
            Makes sense test it?
        """
        pass
