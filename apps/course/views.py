from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "courses" : Course.objects.all()
    }

    return render(request,'course/index.html',context)


def add(request):
    # course = Course.objects.get(id = number)
    print "inside add"
    name = request.POST['name']
    print "inside name"
    desc = request.POST['desc']
    print "inside desc"
    x= {'name' : name,'desc' : desc}
    # errors = Course.objects.basic_validator(request.POST)
    errors = Course.objects.basic_validator(x)
    print errors

    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        course = Course.objects.create(name=name,desc=desc)
    print course
    return redirect('/')


def destroy(request,id):
    # context = {
    #     "courses" : Course.object.get(id = number)
    # }
    return render(request,'course/destroy.html',{"courses": Course.objects.get(id = id)})


def delete(request,id):
    b = Course.objects.get(id= id)
    b.delete()

    return redirect('/')