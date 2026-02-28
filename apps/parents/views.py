from rest_framework import viewsets
from .models import ParentProfile, ParentStudentRelationship
from .serializers import ParentProfileSerializer, ParentStudentRelationshipSerializer

class ParentProfileViewSet(viewsets.ModelViewSet):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentProfileSerializer

class ParentStudentRelationshipViewSet(viewsets.ModelViewSet):
    queryset = ParentStudentRelationship.objects.all()
    serializer_class = ParentStudentRelationshipSerializer
