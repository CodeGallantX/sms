from rest_framework import serializers
from .models import StudentProfile, AdmissionRecord, AcademicHistory, Attendance
from apps.accounts.serializers import UserSerializer

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class_name = serializers.CharField(source='current_class.name', read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
