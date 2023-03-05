# Call model testing module
from django.db import IntegrityError
from django.test import TestCase

from call_billing.models import Call


class CallModelTests(TestCase):

    def test_create_object_with_required_fields_then_success(self):
        """
        Create object with 2 required fields
        """
        obj = Call(call_duration=1, user_name='user_name')
        obj.save()
        self.assertIsNotNone(obj.id)

    def test_create_object_without_user_name_then_failed(self):
        """
        Create object without user_name then get error
        """
        with self.assertRaises(IntegrityError):
            obj = Call(call_duration=1, user_name=None)
            print("aaa", obj.user_name is None)
            obj.save()

    def test_create_object_without_call_duration_then_failed(self):
        """
        Create object without call_duration then get error
        """
        with self.assertRaises(IntegrityError):
            obj = Call(user_name='user_name')
            obj.save()

    def test_timestamps_with_auto_behavior(self):
        """
        Timestamps are set automatically
        """
        obj = Call(call_duration=1, user_name='user_name')
        obj.save()

        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

        self.assertNotEqual(obj.created_at, obj.updated_at)

        """
        updated_at gets auto updated, while created_at stays the same
        """
        obj = Call(call_duration=1, user_name='user_name')
        obj.save()

        original_created_at = obj.created_at
        original_updated_at = obj.updated_at

        obj.save()
        # Get a fresh object
        obj = Call.objects.get(id=obj.id)

        self.assertEqual(original_created_at, obj.created_at)
        self.assertNotEqual(original_updated_at, obj.updated_at)
