from django.contrib import admin
from .models import AcademicYear, Term, Curriculum, Class, Arm, Subject, Exam, ExamScore, ReportCard

admin.site.register(AcademicYear)
admin.site.register(Term)
admin.site.register(Curriculum)
admin.site.register(Class)
admin.site.register(Arm)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(ExamScore)
admin.site.register(ReportCard)
