# Call Service tesing module
from django.test import TestCase

from call_billing.models import Call
from call_billing.services.billing_service import billing_get
from call_billing.services.call_service import call_create
from call_billing.tests.factories import CallFactory


class TestCallService(TestCase):

    def test_create_call(self):
        """
        Test create a new call
        """
        call_duration = 10001
        user_name = "user_name"
        call_create(user_name=user_name, call_duration=call_duration)
        call_result: [Call] = list(Call.objects.filter(user_name=user_name))
        self.assertEqual(len(call_result), 1)
        call_obj = call_result[0]
        self.assertEqual(call_obj.user_name, user_name)
        self.assertEqual(call_obj.call_duration, call_duration)
