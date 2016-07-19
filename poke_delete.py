import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()
from pokemon.models import Pokemon, Trainer, Capture

Pokemon.objects.all().delete()
Trainer.objects.all().delete()
Capture.objects.all().delete()
