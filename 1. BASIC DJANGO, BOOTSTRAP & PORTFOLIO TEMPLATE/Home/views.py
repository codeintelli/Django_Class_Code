from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    # return HttpResponse('Hello World about')
    return render(request,'about.html')

def contact(request):

    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message is sent to admin we can contact you in 24 hours')
    return render(request,'contact.html')

def services(request):
    # return HttpResponse('Hello World feedback')
    return render(request,'services.html')