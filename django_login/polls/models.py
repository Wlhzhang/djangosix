from django.db import models
#

class MyUser(models.Model):
    username = models.CharField('用户名',max_length=30,unique=True)
    userEmail = models.EmailField()
    headimage = models.FileField('头像',upload_to='tmp/')
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'
