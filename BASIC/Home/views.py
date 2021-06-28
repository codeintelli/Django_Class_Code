from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    # return HttpResponse('Hello World about')
    return render(request,'about.html')

def contact(request):
    # return HttpResponse('Hello World contact')
    return render(request,'contact.html')

def feedback(request):
    # return HttpResponse('Hello World feedback')
    return render(request,'feedback.html')