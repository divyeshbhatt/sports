from django import forms
from .models import Competitions, Matches


class CompetitionForm(forms.ModelForm):
	start_from	=	forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
	end_on		=	forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

	class Meta:
		model = Competitions
		fields = '__all__'

class MatchForm(forms.ModelForm):
	class Meta:
		model = Matches
		fields = '__all__'
    
