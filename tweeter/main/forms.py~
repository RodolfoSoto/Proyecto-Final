from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import UserProfile, Tweeet, User


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile

class TweeetForm(forms.ModelForm):
	class Meta:
		model = Tweeet
		exclude = ('author',)

class CreationForm(UserCreationForm):
	email = forms.EmailField(label=("E-mail"), max_length=75)
	class Meta: 
		model = User
		exclude = ('is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions', 'password',)

class EditForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('followers', 'author',)


