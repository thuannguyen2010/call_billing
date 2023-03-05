# Billing API testing module

from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from call_billing.tests.factories import CallFactory


class TestBillingApi(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.client = APIClient()
        self.user_name = "user_name"

    @staticmethod
    def _get_path(user_name: str):
        return f"/mobile/{user_name}/billing"

    def test_api_get_billing_when_user_has_block_without_round_up_then_return_success(self):
        """
        Test api get billing when user has block without round up
        user has 3 calls with durations: 10(s) - 10(s) - 10(s) = 30 (s)
        Expected result: call_count=3, block_count=1
        """
        duration = 10000  # in milliseconds
        CallFactory(user_name=self.user_name, call_duration=duration)
        CallFactory(user_name=self.user_name, call_duration=duration)
        CallFactory(user_name=self.user_name, call_duration=duration)
        get_billing_response = self.client.get(self._get_path(self.user_name))
        self.assertEqual(get_billing_response.status_code, HTTP_200_OK)
        result = get_billing_response.json()
        self.assertEqual(result['call_count'], 3)
        self.assertEqual(result['block_count'], 1)

    def test_api_get_billing_when_user_has_block_with_round_up_then_return_success(self):
        """
        Test api get billing when user has block with round up
        user has 3 calls with durations: 10(s) - 10(s) - 11(s) = 31 (s)
        Expected result: call_count=3, block_count=2
        """
        duration = 10000  # in milliseconds
        CallFactory(user_name=self.user_name, call_duration=duration)
        CallFactory(user_name=self.user_name, call_duration=duration)
        CallFactory(user_name=self.user_name, call_duration=duration + 1)
        get_billing_response = self.client.get(self._get_path(self.user_name))
        self.assertEqual(get_billing_response.status_code, HTTP_200_OK)
        result = get_billing_response.json()
        self.assertEqual(result['call_count'], 3)
        self.assertEqual(result['block_count'], 2)

    def test_api_get_billing_when_user_does_not_have_any_call_then_return_success(self):
        """
        Test api get billing when user doesn't have any call
        Expected result: call_count=0, block_count=0
        """
        get_billing_response = self.client.get(self._get_path(self.user_name))
        self.assertEqual(get_billing_response.status_code, HTTP_200_OK)
        result = get_billing_response.json()
        self.assertEqual(result['call_count'], 0)
        self.assertEqual(result['block_count'], 0)