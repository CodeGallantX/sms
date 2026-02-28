from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from apps.students.models import StudentProfile
from apps.students.services import StudentService
from apps.staff.models import StaffProfile
from apps.parents.models import ParentProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'STUDENT':
            student_number = StudentService.generate_student_number()
            StudentProfile.objects.create(user=instance, student_number=student_number, date_of_birth='2000-01-01') # Placeholder DOB
        elif instance.role == 'TEACHER' or instance.role == 'ACCOUNTANT' or instance.role == 'MANAGEMENT' or instance.role == 'SCHOOL_ADMIN':
            # Auto employee ID generation would go here
            pass
        elif instance.role == 'PARENT':
            ParentProfile.objects.create(user=instance)
