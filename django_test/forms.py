from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	firstname = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	
	class Meta:
		model = User
		fields = ('username','firstname', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.firstname = self.cleaned_data['firstname']

		if commit:
			user.save()

		return user
			
	
