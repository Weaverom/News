from django import forms
from .models import Ad
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'text',
            'category',
        ]


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        group_users = Group.objects.get(name="users")
        user.groups.add(group_users)
        return user
