from django.db import models
from django.contrib.auth.models import AbstractUser
# from myapp.models import ModelBase

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(
        primary_key=True
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='用户名', 
    )
    password = models.CharField(
        max_length=30,
        verbose_name= '密码',
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    gender = models.CharField(max_length=50)#性别
    birthday=models.IntegerField(verbose_name='年龄')#年龄
    image = models.ImageField(max_length=100)#/media/img/上传头像
    created_time = models.DateTimeField(null=True)#创建时间
    last_login = models.DateTimeField(null=True)#登录时间

    class Meta:
        db_table = "user_info"  # 指明数据库表名

    def __str__(self):  # 这个__str__方法的作用将在查询时看到
        return f'User<id={self.id},username={self.username},email={self.email}'


class Special_edition(models.Model):
    Edname = models.CharField(max_length = 255 )
    Edinfo = models.CharField(max_length = 255 )
    created_time = models.DateTimeField(null=True)
    user_id = models.ForeignKey( to= User ,on_delete=models.CASCADE,db_column='user_id')

    class Meta:
        db_table = "special_edition"

    def __str__(self):
        return f'Edname={self.Edname},Edinfo={self.Edinfo},created_time={self.created_time},user_id={self.user_id.id}'