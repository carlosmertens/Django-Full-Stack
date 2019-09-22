from django import forms
from django.core import validators

# Create Manually a name validator. Start with capital letter


def check_for_z(value):
    """Function to verify that name starts with capital letter."""

    if value[0] not in 'QWERTZUIOPLKJHGFDSAYXCVBNM':
        raise forms.ValidationError("Name needs to start with capital letter!")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    # Field to type email again for verification purpose
    verify_email = forms.EmailField(label='Verify your email')
    text = forms.CharField(widget=forms.Textarea)

    # #Create manually a bot catcher
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!!!")
    #     return botcatcher

    # Clean all fields

    def clean(self):
        """Function to verify email address."""

        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Please verify your email address!")

    # Create a bot cacher using Django built-in Validators
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
