from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        # 验证是否有用户名
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password):
        # 设置超级用户
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField('用户名',max_length=30,unique=True)
    userEmail = models.EmailField('邮箱')
    headimage = models.FileField('头像',upload_to='tmp/')
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    # is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # 创建超级用户时使用

    #
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    class Meta:
        db_table = 'user'
