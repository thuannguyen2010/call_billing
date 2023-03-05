import logging

from call_billing.models import Call

_logger = logging.getLogger(__name__)


def call_create(user_name: str, call_duration: int):
    """
    Create call data
    """
    _logger.info(f"CallService - call create - user_name={user_name}, call_duration={call_duration}")
    Call.objects.create(user_name=user_name, call_duration=call_duration)
