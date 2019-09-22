from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    # CREATE A BOT CATCHER MANUALLY
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!!!")
    #     return botcatcher

    # Create a bot cacher using Django built-in Validators
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
