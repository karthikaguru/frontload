from django.forms import ModelForm
from frontapp.models import product,order

# Create your models here.
class productForm(ModelForm):
    class Meta:
        model=product
        fields="__all__"
    

class orderForm(ModelForm):
    class Meta:
        model=order
        fields="__all__"
    

   