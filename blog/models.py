import re
from django.db import models
from django.utils import timezone
from django.forms import ValidationError

# Create your models here.

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise ValidationError('Invalid Lnglat Type')

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Mark Down 문법을 써주세요')
    tags = models.CharField(max_length=100,blank=True)
    photo = models.ImageField(blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    test_field = models.IntegerField(default=10)

    def __str__(cls):
        return cls.title
