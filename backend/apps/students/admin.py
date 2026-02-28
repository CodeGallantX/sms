from django.contrib import admin
from .models import StudentProfile, AdmissionRecord, AcademicHistory, Attendance

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'user', 'current_class', 'admission_date')
    search_fields = ('student_number', 'user__email', 'user__first_name')

admin.site.register(AdmissionRecord)
admin.site.register(AcademicHistory)
admin.site.register(Attendance)
