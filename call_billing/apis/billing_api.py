from rest_framework import serializers
from rest_framework.views import APIView, Response

from call_billing.services.billing_service import billing_get


class BillingGetApi(APIView):
    class OutputSerializer(serializers.Serializer):
        call_count = serializers.IntegerField()
        block_count = serializers.IntegerField()

    def get(self, request, user_name):
        billing_data = billing_get(user_name)
        data = self.OutputSerializer(billing_data).data
        return Response(data)
