from django.db import models
from django.conf import settings

class FeeStructure(models.Model):
    name = models.CharField(max_length=255)
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()

class Invoice(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE, related_name='invoices')
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=(('PENDING', 'Pending'), ('PARTIAL', 'Partial'), ('PAID', 'Paid'), ('OVERDUE', 'Overdue')))
    installment_plan = models.BooleanField(default=False)

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50) # Cash, Transfer, Card
    transaction_id = models.CharField(max_length=100, unique=True)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Scholarship(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE)

class Expense(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Budget(models.Model):
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE)
    department = models.ForeignKey('staff.Department', on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2)
    spent_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
