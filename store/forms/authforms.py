
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="First Name")#manipulating the label 
    last_name = forms.CharField(required=True, label="Last Name")#manipulating the label
    
    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if len(value.strip()) < 3 :
            raise ValidationError("First Name Must Be 3 Char Long...")
        return value.strip()


    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if len(value.strip()) < 3 :
            raise ValidationError("Last Name Must Be 3 Char Long...")
        return value.strip()


    class Meta:
        model = User  #django in built User model   
        fields = ['username', 'first_name', 'last_name']
#so, from where this firstname and last name come so it is present in 
# User model of django we only need to call it from User model 
#first_name and last_name will be same ditto because it is predefined class of User model