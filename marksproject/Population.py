import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marksproject.settings')

import django
django.setup()

from marksapp.models import Student
from faker import Faker
import random

fake = Faker()

def populate(N=5):
    for i in range(N):
        fake_name = fake.name()
        fake_sec = random.randint(1,12)
        fake_marks = random.randint(0,100)
        fake_emails = fake.email()

        student_entry = Student.objects.get_or_create(Name=fake_name, Section=fake_sec, Email=fake_emails, Marks_obtained=fake_marks)
    
populate(10)