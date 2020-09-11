from django.shortcuts import render
from information.models import Information
from information.models import HomePage
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    info_lists=HomePage.objects.order_by('title')
    descp={'access_record':info_lists}
    return render(request,'index.html', context=descp)

def header(request):
    return render(request,'header.html')

def page1(request):
    return render(request,'page1.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def page4(request):
    return render(request,'page4.html')

def page5(request):
    return render(request,'page5.html')

def page6(request):
    return render(request,'page6.html')

def aboutme(request):
    return render(request,'aboutme.html')


def latestpost(request):
    info_list=Information.objects.order_by('description')
    desc={'access_records':info_list}
    return render(request,'latestpost.html', context=desc)

