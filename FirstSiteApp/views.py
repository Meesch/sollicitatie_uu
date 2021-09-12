from django.shortcuts import render
from django.shortcuts import HttpResponse

def homepage(request):
    return render(request, 'FirstSiteApp/homepage.html')
    # return HttpResponse("Hey")


def contact(request):
    return render(request, 'FirstSiteApp/contact.html')

def CV(request):
    return render(request, 'FirstSiteApp/CV.html')

def geesteswetenschapper(request):
    return render(request, 'FirstSiteApp/geesteswetenschapper.html')

def informaticus(request):
    return render(request, 'FirstSiteApp/informaticus.html')

def onderzoeker(request):
    return render(request, 'FirstSiteApp/onderzoeker.html')