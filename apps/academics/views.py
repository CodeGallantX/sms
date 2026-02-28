from rest_framework import viewsets
from .models import Class, Subject, Exam, ExamScore, ReportCard
from .serializers import ClassSerializer, SubjectSerializer, ExamScoreSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ExamScoreViewSet(viewsets.ModelViewSet):
    queryset = ExamScore.objects.all()
    serializer_class = ExamScoreSerializer
