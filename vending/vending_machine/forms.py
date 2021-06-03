from django.forms import ModelForm
from .models import coins



class coin_form(ModelForm):
    class Meta:
        model= coins
        fields='__all__'



