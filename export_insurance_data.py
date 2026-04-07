import sys
import os
import csv

# Add current directory (project root) to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rcm_project.settings')

import django
django.setup()

from medical_records.models import InsuranceClaim

with open('insurance_claims.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['claim_amount', 'patient_age', 'approved', 'provider'])

    for claim in InsuranceClaim.objects.all():
        writer.writerow([
            float(claim.claim_amount),
            claim.patient.age if claim.patient else 0,
            1 if claim.approved else 0,
            claim.provider
        ])
