# Call API testing module

from django.test import TestCase
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.test import APIClient

from call_billing.models import Call


class TestCallApi(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.client = APIClient()

    @staticmethod
    def _get_path(user_name: str):
        return f"/mobile/{user_name}/call"

    def test_api_create_call_when_length_of_user_name_is_greater_than_32_then_return_failed(self):
        """
        Test api create a new call when length of user_name is greater than 32 then return failed
        user_name=123456789012345678901234567890123
        call_duration=1000
        """
        user_name = "123456789012345678901234567890123"
        create_call_response = self.client.put(self._get_path(user_name), format='json', data={
            "call_duration": 1000
        })
        self.assertEqual(create_call_response.status_code, HTTP_400_BAD_REQUEST)

    def test_api_create_call_when_user_name_contains_invalid_character_then_return_failed(self):
        """
        Test api create a new call when user_name contains invalid character then return failed
        user_name=abc!
        call_duration=1000
        """
        user_name = "abc!"
        create_call_response = self.client.put(self._get_path(user_name), format='json', data={
            "call_duration": 1000
        })
        self.assertEqual(create_call_response.status_code, HTTP_400_BAD_REQUEST)

    def test_api_create_call_when_call_duration_is_smaller_than_0_then_return_failed(self):
        """
        Test api create a new call when call_duration is smaller than 0 then return failed
        user_name=abc!
        call_duration=1000
        """
        user_name = "abc"
        create_call_response = self.client.put(self._get_path(user_name), format='json', data={
            "call_duration": -1
        })
        self.assertEqual(create_call_response.status_code, HTTP_400_BAD_REQUEST)

    def test_api_create_call_when_all_parameters_are_valid_then_return_success(self):
        """
        Test api create a new call when all parameters are valid then return success
        """
        user_name = "abc"
        create_call_response = self.client.put(self._get_path(user_name), format='json', data={
            "call_duration": 10000
        })
        self.assertEqual(create_call_response.status_code, HTTP_200_OK)

        # Check data in database
        call_obj: Call = Call.objects.filter(user_name=user_name).first()
        self.assertEqual(call_obj.call_duration, 10000)
        self.assertEqual(call_obj.user_name, user_name)

        # Create a new call with the same user
        create_call_response = self.client.put(self._get_path(user_name), format='json', data={
            "call_duration": 20000
        })
        self.assertEqual(create_call_response.status_code, HTTP_200_OK)

        # Check in database
        call_obj_count: Call = Call.objects.filter(user_name=user_name).count()
        self.assertEqual(call_obj_count, 2)
