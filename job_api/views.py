from django.shortcuts import render

# Create your views here.
# Create your views here.
from job_api.models import job
from job_api.serializers import jobSerializer

from rest_framework import viewsets


# Create your views here.
class jobViewSet(viewsets.ModelViewSet):
    queryset = job.objects.all()
    serializer_class = jobSerializer