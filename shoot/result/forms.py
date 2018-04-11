from django import forms
from django.forms.models import modelformset_factory
from .models import Result

class Result1Form(forms.ModelForm):
	class Meta:
		model = Result
		fields = ('competition_id', 'shooter_id',)

ResultFormSet=modelformset_factory(Result, form=Result1Form, max_num=3)

class Result2Form(forms.ModelForm):
	class Meta:
		model = Result
		fields = ('match_id',)

class ScoreForm(forms.ModelForm):
	s1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s3 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s4 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s5 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s6 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s7 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s8 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s9 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s10 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s14 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s15 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s16 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s17 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s18 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s19 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s20 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s24 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s25 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s26 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s27 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s28 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s29 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s30 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s34 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s35 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s36 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s37 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s38 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s39 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	s40 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

	class Meta:
		model = Result
		fields = ('s1',
				's2',
				's3',
				's4',
				's5',
				's6',
				's7',
				's8',
				's9',
				's10',
				's11',
				's12',
				's13',
				's14',
				's15',
				's16',
				's17',
				's18',
				's19',
				's20',
				's21',
				's22',
				's23',
				's24',
				's25',
				's26',
				's27',
				's28',
				's29',
				's30',
				's31',
				's32',
				's33',
				's34',
				's35',
				's36',
				's37',
				's38',
				's39',
				's40',)
