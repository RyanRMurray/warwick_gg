from django import forms
from django.contrib.auth.models import User

from uwcs_auth.models import WarwickGGUser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = WarwickGGUser
        fields = ['nickname', 'steam_user', 'battle_net_user']
        widgets = {
            'steam_user': forms.TextInput(attrs={'placeholder': 'None set'}),
            'battle_net_user': forms.TextInput(attrs={'placeholder': 'None set'})
        }


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class DeleteUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['email']


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    uni_id = forms.CharField(max_length=11,
                             help_text='If you are an associate member then use the ID provided by the SU')
    nickname = forms.CharField(max_length=50, required=False)
    privacy_policy_read = forms.BooleanField()

    def signup(self, request, user):
        pass
