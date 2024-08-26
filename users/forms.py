from django import forms
from django.core.exceptions import ValidationError # 검증오류 에러
from users.models import User # User 모델과 중복되는지 확인

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        widget=forms.TextInput(
            attrs = {"placeholder" : "username (4자리 이상)"}
        ))
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs = {"placeholder" : "password (4자리 이상)"}
        ))
    
class SignupForm(forms.Form):
    username = forms.CharField(min_length=4)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username = username).exists():
            raise ValidationError(f"입력한 username ({username})은 이미 사용중입니다.")
        
        return username
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            # password2 필드에 오류를 추가
            self.add_error("password2", "비밀번호화 비밀번호 확인값이 다릅니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]

        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_description = short_description,

        )
        return user