# Billing Service testing module
from django.test import TestCase

from call_billing.services.billing_service import billing_get
from call_billing.tests.factories import CallFactory


class TestBillingService(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user_name = "user_name"

    def test_billing_get_without_round_up_block(self):
        """
        User has 3 calls with total duration is 30s
        Then return call_count=3 and block_count=1
        """
        CallFactory(user_name=self.user_name, call_duration=10000)
        CallFactory(user_name=self.user_name, call_duration=10000)
        CallFactory(user_name=self.user_name, call_duration=10000)

        billing_data = billing_get(self.user_name)
        self.assertEqual(billing_data.call_count, 3)
        self.assertEqual(billing_data.block_count, 1)

    def test_billing_get_with_round_up_block(self):
        """
        User has 3 calls with total duration is 36s
        Then return call_count=3 and block_count=1
        """
        CallFactory(user_name=self.user_name, call_duration=10000)
        CallFactory(user_name=self.user_name, call_duration=10000)
        CallFactory(user_name=self.user_name, call_duration=16000)

        billing_data = billing_get(self.user_name)
        self.assertEqual(billing_data.call_count, 3)
        self.assertEqual(billing_data.block_count, 2)

    def test_billing_of_a_user_does_not_have_any_call(self):
        """
        User has 3 calls with total duration is 36s
        Then return call_count=3 and block_count=1
        """
        billing_data = billing_get(self.user_name)
        self.assertEqual(billing_data.call_count, 0)
        self.assertEqual(billing_data.block_count, 0)
