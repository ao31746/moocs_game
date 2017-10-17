from django.shortcuts import render
from games.models import ROFR_model, JUDO_model,Company_Merger_model,Price_War_model
from games.serializers import ROFR_Serializer, JUDO_Serializer,Company_Merger_Serializer, Price_War_Serializer

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
def Company_Merger(request):
    return render(request, 'Company_Merger.html', {
        'data': "Hello Django ",
    })
def Price_War(request):
    return render(request, 'Price_War.html', {
        'data': "Hello Django ",
    })

def jump(request):
    return render(request, 'jump.html', {
        'data': "Hello Django ",
    })

class ROFR_ViewSet(viewsets.ModelViewSet):
    queryset = ROFR_model.objects.all()
    serializer_class = ROFR_Serializer
class JUDO_ViewSet(viewsets.ModelViewSet):
    queryset = JUDO_model.objects.all()
    serializer_class = JUDO_Serializer
class Company_Merger_ViewSet(viewsets.ModelViewSet):
    queryset = Company_Merger_model.objects.all()
    serializer_class = Company_Merger_Serializer
class Price_War_ViewSet(viewsets.ModelViewSet):
    queryset = Price_War_model.objects.all()
    serializer_class = Price_War_Serializer