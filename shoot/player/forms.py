from django import forms
from .models import Player
DATE_FORMAT = 'N j, Y'


class PlayerForm(forms.ModelForm):
	birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
	class Meta:
		model = Player
		fields = '__all__'
