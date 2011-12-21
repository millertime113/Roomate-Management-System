from django import forms
from myModels import dbAccess

class AddTransaction(forms.Form):
    user = forms.ChoiceField(choices=dbAccess.getUsersForChoiceField())
    amount = forms.DecimalField(min_value = 0.01, decimal_places = 2)
    description = forms.CharField(widget = forms.Textarea, max_length = 1000, required=true)