from django.shortcuts import render

# Create your views here.


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'abc123/index.html')


# def webapge2(request):
#     #return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'abc123/webpage2.html')