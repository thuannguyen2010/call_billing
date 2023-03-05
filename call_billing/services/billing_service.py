# Services for handling business logic and pushing data to database
from dataclasses import dataclass

from django.db.models import Count, Sum

from call_billing.models import Call

NUM_OF_SECONDS_EACH_BLOCK = 30 * 1000  # in milliseconds


@dataclass
class BillingData:
    call_count: int = 0
    block_count: int = 0


def billing_get(user_name: str) -> BillingData:
    """
    Get billing of a user by number blocks of duration
    """
    call_queryset = Call.objects.filter(user_name=user_name).values('user_name').annotate(
        call_count=Count('id'),
        duration_sum=Sum('call_duration')
    )
    billing_data = BillingData()
    if call_queryset:
        call_data = list(call_queryset)[0]
        billing_data.call_count = call_data['call_count']
        billing_data.block_count = call_data['duration_sum'] // NUM_OF_SECONDS_EACH_BLOCK + \
                                   (call_data['duration_sum'] % NUM_OF_SECONDS_EACH_BLOCK > 0)
    return billing_data
