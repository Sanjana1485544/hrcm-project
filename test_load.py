import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rcm_project.settings')
django.setup()

from medical_records.models import MedicalProvider

print('Successfully imported MedicalProvider model!')
