from django import forms
from django.core.validators import MinValueValidator


class FibonacciForm(forms.Form):
	n = forms.IntegerField(
			widget=forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder': 'Type the value of N here',
				}
			),
			validators=[MinValueValidator(0)],
			help_text="Enter an integer number N to show the nth fibonacci number"
		)
