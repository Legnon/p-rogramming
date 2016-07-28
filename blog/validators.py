import re
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(self.min_length))

'''
closure를 통해 만든 함수는 그 함수에서만 사용 가능하기 때문에 makemigrations가 안되고
따라서 class를 이용해서 만드는게 맞다.
def min_length_validator(min_length):
    def wrap(value):
        if len(value) < min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(min_length))
    return wrap
'''

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise ValidationError('Invalid Lnglat Type')


def phone_number_validator(value):
    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')
