from django.db import models
from django.conf import settings
from django.utils import timezone

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    student_number = models.CharField(max_length=20, unique=True, editable=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')))
    admission_date = models.DateField(default=timezone.now)
    current_class = models.ForeignKey('academics.Class', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    medical_info = models.TextField(blank=True)
    behavior_log = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_number})"

class AdmissionRecord(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    previous_school = models.CharField(max_length=255, blank=True)
    admission_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    documents = models.FileField(upload_to='admissions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AcademicHistory(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='academic_history')
    institution = models.CharField(max_length=255)
    qualification = models.CharField(max_length=100)
    year_completed = models.IntegerField()
    grade = models.CharField(max_length=10)

class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('LATE', 'Late')))
    remarks = models.TextField(blank=True)

    class Meta:
        unique_together = ('student', 'date')
