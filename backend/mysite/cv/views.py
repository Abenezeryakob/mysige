from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import EducationSerializer
from .models import Experience

def homeView(request):
    return render(request, './home.html')

class ExprienceDetailApi(APIView):

    queryset = Experience.objects.all()
    serializer_class = EducationSerializer
