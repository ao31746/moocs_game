from django.shortcuts import render
from games.models import ROFR_model, JUDO_model
from games.serializers import ROFR_Serializer, JUDO_Serializer

from rest_framework import viewsets
# Create your views here.
def ROFR(request):
    return render(request, 'ROFR.html', {
        'data': "Hello Django ",
    })
def JUDO(request):
    return render(request, 'JUDO.html', {
        'data': "Hello Django ",
    })

class ROFR_ViewSet(viewsets.ModelViewSet):
    queryset = ROFR_model.objects.all()
    serializer_class = ROFR_Serializer

class JUDO_ViewSet(viewsets.ModelViewSet):
    queryset = JUDO_model.objects.all()
    serializer_class = JUDO_Serializer