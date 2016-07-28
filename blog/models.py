import re
from django.db import models
from django.utils import timezone
from django.forms import ValidationError
from .validators import MinLengthValidator, lnglat_validator


min_length3_validator = MinLengthValidator(3)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(cls):
        return cls.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', validators=[min_length3_validator])
    content = models.TextField(help_text='Mark Down 문법을 써주세요')
    tags = models.ManyToManyField(Tag, blank=True)
    # tags = models.CharField(max_length=10)
    photo = models.ImageField(blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    test_field = models.IntegerField(default=10)

    def __str__(cls):
        return cls.title

