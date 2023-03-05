from factory.django import DjangoModelFactory


class CallFactory(DjangoModelFactory):
    class Meta:
        model = "call_billing.Call"

    user_name = "user_name"
    call_duration = 30000
