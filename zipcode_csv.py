import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from blog.models import ZipCode

import csv

CSV = '20150710_seoul.txt'

reader = csv.reader(open(CSV, 'rt', encoding='cp949'), delimiter='|')

columns = next(reader)
print(columns)
zipcode_list = []

for idx, row in enumerate(reader):
    data = dict(zip(columns, row))
    print(data)
    zip_code = ZipCode(
        city=data['시도'], road=data['도로명'], dong=data['법정동명'],
        gu=data['시군구'], code=data['우편번호'])
    zipcode_list.append(zip_code)

ZipCode.objects.bulk_create(zipcode_list, 100)
