from django.shortcuts import render

# Create your views here.
def ROFR(request):
    return render(request, 'ROFR.html', {
        'data': "Hello Django ",
    })
def JUDO(request):
    return render(request, 'JUDO.html', {
        'data': "Hello Django ",
    })  
