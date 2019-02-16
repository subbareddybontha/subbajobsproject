from django.shortcuts import render
from testapp.models import Hydjobs,Bangjobs,Chennaijobs,Punejobs

# Create your views here.
def homehtml(request):
    return render(request, 'testapp/homejobs.html')
def Hyd_jobs_views(request):
    hydjobs_list=Hydjobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'hydjobs_list':hydjobs_list})
def Bang_jobs_views(request):
    Bangjobs_list=Bangjobs.objects.all()
    return render(request,'testapp/bangjobs.html',{'Bangjobs_list':Bangjobs_list})
def Chennai_jobs_views(request):
    Chennaijobs_list=Chennaijobs.objects.all()
    return render(request,'testapp/chennaijobs.html',{'Chennajobs_list':Chennaijobs_list})
def Pune_jobs_views(request):
    Punejobs_list=Punejobs.objects.all()
    return render(request,'testapp/punejobs.html',{'Punejobs_list':Punejobs_list})
