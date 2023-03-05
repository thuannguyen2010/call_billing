# Billing API module
from rest_framework import serializers
from rest_framework.views import APIView, Response

from call_billing.services.billing_service import billing_get
import logging
_logger = logging.getLogger(__name__)

class BillingGetApi(APIView):
    class OutputSerializer(serializers.Serializer):
        call_count = serializers.IntegerField()
        block_count = serializers.IntegerField()

    def get(self, request, user_name):
        _logger.info(f"BillingAPI - billing get - user_name={user_name}")
        billing_data = billing_get(user_name)
        data = self.OutputSerializer(billing_data).data
        return Response(data)
