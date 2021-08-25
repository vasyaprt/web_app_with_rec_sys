from .models import Order
from bootstrap_modal_forms.forms import BSModalModelForm

class OrderModelForm(BSModalModelForm):

    class Meta:
        model = Order
        fields = ['time', 'msg']

