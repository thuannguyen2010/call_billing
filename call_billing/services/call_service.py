from call_billing.models import Call


def call_create(user_name: str, call_duration: int):
    """
    Create call data
    """
    Call.objects.create(user_name=user_name, call_duration=call_duration)