from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserWeightModel


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# class UserWeightForm(forms.ModelForm):
#     class Meta:
#         model = UserWeightModel
#         fields = ("weight",)

    # def save(self, commit=True):
    #     user_weight = super(UserWeightForm, self).save(commit=False)
    #     user_weight.user_id = self.request.user.id
    #     user_weight.weight = self.cleaned_data['weight']
    #
    #     if commit:
    #         user_weight.save()
    #     return user_weight
