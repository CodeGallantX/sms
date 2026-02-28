from django.db import models
from django.conf import settings

class ParentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='parent_profile')
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.phone_number})"

class ParentStudentRelationship(models.Model):
    parent = models.ForeignKey(ParentProfile, on_delete=models.CASCADE, related_name='student_relationships')
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE, related_name='parent_relationships')
    relationship_type = models.CharField(max_length=20, choices=(('FATHER', 'Father'), ('MOTHER', 'Mother'), ('GUARDIAN', 'Guardian')))

    class Meta:
        unique_together = ('parent', 'student')

class FeeReminder(models.Model):
    parent = models.ForeignKey(ParentProfile, on_delete=models.CASCADE, related_name='fee_reminders')
    invoice = models.ForeignKey('finance.Invoice', on_delete=models.CASCADE)
    sent_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
