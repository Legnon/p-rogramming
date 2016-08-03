import re
import requests
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
from django.conf import settings


EPOST_API_KEY = settings.EPOST_API_KEY

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


@deconstructible
class zipcode_validator(object):
    def __init__(self, is_check_exist=False):
        self.is_check_exist = is_check_exist

    def __call__(self, value):
        if not re.match(r'^\d{5,6}$', value):
            raise ValidationError('5자리 혹은 6자리 숫자로 입력해주세요.')

        if self.is_check_exist:
            print('$$$$$')
            self.check_exist_from_db(value)
        else:
            print('#####')
            self.check_exist(value)

    def check_exist_from_db(self, value):
        if not ZipCode.objects.filter(code=value).exists():
            raise ValidationError('없는 우편번호입니다.')

    def check_exist(self, value):
        params = {
            'regkey': EPOST_API_KEY,
            'target': 'postNew',
            'query': value,
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response = xmltodict.parse(xml)
        print(response)
        try:
            error = response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))


