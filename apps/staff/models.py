from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class StaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bank_account = models.CharField(max_length=100, blank=True)
    joined_date = models.DateField()
    is_active = models.BooleanField(default=True)

class Payroll(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, related_name='payrolls')
    month = models.IntegerField()
    year = models.IntegerField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(null=True, blank=True)
    payslip_url = models.URLField(blank=True)

class LeaveRequest(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=20, choices=(('SICK', 'Sick'), ('ANNUAL', 'Annual'), ('OTHER', 'Other')))
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')))
    reason = models.TextField()

class PerformanceReview(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField() # 1-5
    comments = models.TextField()
