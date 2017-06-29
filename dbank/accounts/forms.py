from django.forms import ModelForm, ModelChoiceField

from .models import Account, Transaction


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['iban']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        self.owner = owner
        super(AccountForm, self).__init__(*args, **kwargs)




