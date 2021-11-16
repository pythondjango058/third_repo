from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyjobs(request):
    x='<h1>Thousands of jobs available in hyderabad</h1>'
    return HttpResponse(x)
def bangjobs(manisha):
    y='<h1>Awesome jobs available in banglure</h1>'
    return HttpResponse(y)
def punejobs(vishwa):
    z='<h1>in maharasthra most of the jobs available in pune</h1>'
    return HttpResponse(z)
