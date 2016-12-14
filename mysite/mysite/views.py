#-*- coding:utf-8 -*-
#from django.http import HttpResponse
#from django.conf.urls import patterns, include, url
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def max(request):
    max=int(request.GET.get("a",10))
    b=int(request.GET.get("b",5))
    #b=int(request.REQUEST.get("b",5))
    #max = a
    if max < b:
        max = b
    max = max + 1
    if max == 10:
        return HttpResponse(max)
        #return HttpResponseRedirect("max?a={}".format(max))
    else:
        return HttpResponseRedirect("max?a={}".format(max))
        #return HttpResponse(max)