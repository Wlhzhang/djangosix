import re
from django import forms


from polls.models import MyUser


class UserForm(forms.ModelForm):
        class Meta:
            model = MyUser
            fields = [
                'username', 'password','userEmail','headimage'
            ]
            error_messages ={
                'username':{'max_length': '用户名最大长度超出8个字符','min_length': '用户名最小长度至少为5个字符'},
                'password':{'max_length': '密码最大长度超出20个字符', 'min_length': '密码最小长度至少为6个字符'},
                # 'userEmail':{''}
            }
        def clean_username(self):
            regex=r'\w{5,8}'
            if re.findall(regex,self.cleaned_data["username","password"]) is None:
                raise forms.ValidationError('输入格式不正确')
            return self.cleaned_data["username","password"]
