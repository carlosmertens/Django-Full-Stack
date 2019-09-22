from django import forms
from django.core import validators

# Create Manually a name validator. Start with capital letter


def check_for_z(value):
    if value[0] not in 'QWERTZUIOPLKJHGFDSAYXCVBNM':
        raise forms.ValidationError("Name needs to start with capital letter!")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    # #Create manually a bot catcher
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!!!")
    #     return botcatcher

    # Create a bot cacher using Django built-in Validators
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
