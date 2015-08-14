from django import forms
from .models import Event



class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('orginazer','views','created','modified',)
		widgets={

		'name' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'nombre del evento'}),
		'summary' : forms.Textarea(attrs={'class':'form-control','rows':'3','placeholder':'resumen del evento'}),
		'content' : forms.Textarea(attrs={'class':'form-control','rows':'3','placeholder':'contenido del evento'}),
		'category' : forms.Select(attrs={'class':'form-control','placeholder':'categoria del evento'}),
		'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'lugar del evento'}),
		'start' : forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
		'finish' : forms.DateTimeInput(attrs={'class':'form-control','type':'date','placeholder':'nombre del evento'}),
		'imagen' : forms.ClearableFileInput(attrs={'class':'form-control'}),
		'is_free' : forms.CheckboxInput(attrs={'class':'form-control'}),
		'amount' : forms.NumberInput(attrs={'class':'form-control'}),
		#'orginazer' : forms.Select(attrs={'class':'form-control'})

		}



	
