from django import forms

from models import BaseProfile

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    class Meta:
        fields = ('phone', 'xmpp', 'alt_nick', )
        model = BaseProfile
