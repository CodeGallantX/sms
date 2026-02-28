import uuid
from django.utils import timezone
from .models import StudentProfile

class StudentService:
    @staticmethod
    def generate_student_number():
        year = timezone.now().year
        count = StudentProfile.objects.filter(admission_date__year=year).count() + 1
        return f"STU-{year}-{count:04d}"

    @staticmethod
    def enroll_student(user_data, student_data):
        # Implementation for atomical creation of user and student profile
        pass
