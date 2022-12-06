from order.models import Order
from django.forms import (
    ModelForm,
    ChoiceField
)


class PortalForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'status',
        )
