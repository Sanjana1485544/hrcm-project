
from django.db import models

class MedicalProvider(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField()
    pin_code = models.CharField(max_length=10, null=True, blank=True)  # <-- Add this line
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    PURPOSE_CHOICES = [
        ('Checkup', 'Checkup'),
        ('Surgery', 'Surgery'),
        ('Consultation', 'Consultation'),
        ('Follow-up', 'Follow-up'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    doctor_name = models.CharField(max_length=255)
    reason = models.TextField()
    purpose = models.CharField(max_length=100, choices=PURPOSE_CHOICES, default='Checkup')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_date}"




class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    date = models.DateField()
    provider = models.ForeignKey(MedicalProvider, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"History of {self.patient.name} on {self.date}"

class InsuranceClaim(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=20)
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Insurance Claim for {self.patient.name}"

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bill_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Billing for {self.patient.name} on {self.bill_date}"

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.medication_name} for {self.patient.name}"

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment by {self.patient.name} on {self.payment_date}"

class MedicalTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    test_date = models.DateField()
    result = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.test_name} for {self.patient.name} on {self.test_date}"

