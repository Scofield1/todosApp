from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TodoModelForm(forms.ModelForm):
    task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Add you task...'}))
    class Meta:
        model = TodoModel
        fields = ['task',]

class UpdateTodoForm(forms.ModelForm):
    task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Add you task...'}))
    class Meta:
        model = TodoModel
        fields = ['task','complete']