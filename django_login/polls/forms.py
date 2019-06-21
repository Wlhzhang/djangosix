import re
from django import forms


from polls.models import MyUser


class UserForm(forms.ModelForm):
        class Meta:
            model = MyUser
            fields = [
                'username', 'password','userEmail','headimage'
            ]
            username = forms.CharField(max_length=30, min_length=4, required=True,
                                       error_messages={'max_length': '用户名最大长度超出30个字符',
                                                       'min_length': '用户名最小长度至少为5个字符', })
            password = forms.CharField(max_length=30, min_length=5, required=True,
                                       error_messages={'max_length': '密码最大长度超出10个字符',
                                                       'min_length': '密码最小长度至少为6个字符'})

        def clean_username(self):
            regex=r'\w{4,8}'
            if re.findall(regex,self.cleaned_data["username"]) is None:
                raise forms.ValidationError('输入格式不正确')
            return self.cleaned_data["username"]

        def clean_my_file(self):
            return self.cleaned_data['my_file']