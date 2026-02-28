from rest_framework import serializers
from .models import ParentProfile, ParentStudentRelationship
from apps.accounts.serializers import UserSerializer

class ParentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ParentProfile
        fields = '__all__'

class ParentStudentRelationshipSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)

    class Meta:
        model = ParentStudentRelationship
        fields = '__all__'
