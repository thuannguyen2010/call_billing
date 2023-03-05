# Define api routes
from django.urls import path

from call_billing.apis.billing_api import BillingGetApi
from call_billing.apis.call_api import CallCreateApi

urlpatterns = [
    path(
        "mobile/<str:user_name>/call",
        CallCreateApi.as_view(),
        name="create-call"
    ),
    path(
        "mobile/<str:user_name>/billing",
        BillingGetApi.as_view(),
        name="billing-get"
    ),
]
