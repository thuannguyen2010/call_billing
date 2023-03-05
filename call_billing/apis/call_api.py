# Call API
import logging

from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.views import APIView, Response

from call_billing.services.call_service import call_create

_logger = logging.getLogger(__name__)


class CallCreateApi(APIView):
    class RequestSerializer(serializers.Serializer):
        call_duration = serializers.IntegerField(min_value=0)
        user_name = serializers.CharField(min_length=1, max_length=32,
                                          validators=[
                                              RegexValidator(
                                                  r"^[A-Za-z0-9_-]+$",
                                                  message="This value may contain only letters, numbers, - and _"
                                              )])

    class OutputSerializer(serializers.Serializer):
        code = serializers.CharField()
        message = serializers.CharField()

    def put(self, request, user_name):
        _logger.info(f"CallAPI - call create - user_name={user_name}")
        request.data.update(user_name=user_name)
        create_request_serializer = self.RequestSerializer(data=request.data)
        create_request_serializer.is_valid(raise_exception=True)
        call_create(**create_request_serializer.validated_data)
        data = self.OutputSerializer({
            "code": "success",
            "message": "Success"
        }).data
        return Response(data)
