from django.db import models
from django.conf import settings

class AcademicYear(models.Model):
    name = models.CharField(max_length=50) # e.g. 2024/2025
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

class Term(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=50) # e.g. First Term
    start_date = models.DateField()
    end_date = models.DateField()

class Curriculum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Class(models.Model):
    name = models.CharField(max_length=100) # e.g. Grade 1
    curriculum = models.ForeignKey(Curriculum, on_delete=models.SET_NULL, null=True, blank=True)
    class_teacher = models.ForeignKey('staff.StaffProfile', on_delete=models.SET_NULL, null=True, related_name='classes_taught')

class Arm(models.Model):
    name = models.CharField(max_length=10) # e.g. A, B, Blue, Gold
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='arms')

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

class Timetable(models.Model):
    arm = models.ForeignKey(Arm, on_delete=models.CASCADE, related_name='timetables')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    arm = models.ForeignKey(Arm, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    max_score = models.IntegerField()

class Exam(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50) # e.g. Final, Mid-term
    date = models.DateField()
    max_score = models.IntegerField()

class ExamScore(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='scores')
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(blank=True)

class ReportCard(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    rank = models.IntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)
