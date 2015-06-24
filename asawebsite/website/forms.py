from django import forms 

class JoinForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=50)
	last_name = forms.CharField(label='Last Name', max_length=50)
	andrew_id = forms.CharField(label='Andrew ID', max_length=100)