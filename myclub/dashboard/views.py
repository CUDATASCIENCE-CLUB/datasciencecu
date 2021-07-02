from django.shortcuts import render,redirect
from .models import events,thread,replies
from django.contrib.auth.models import User
from accounts.models import member
from postman.models import Message
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import datetime


def ev(request):
    u = User.objects.get(username=request.user.get_username())
    bi = member.objects.get(user=u)
    event = events.objects.all().order_by('-date')
    ev = events.objects.all().count()
    recipien = User.objects.get(username=request.user.get_username())
    receiver = Message.objects.filter(recipient=recipien)
    rec_no=  Message.objects.filter(recipient=recipien).count()
    e = events.objects.all().order_by('-date')
    p= Paginator(events.objects.all().order_by('-date','-time'),6)
    page = request.GET.get('page')
    venue= p.get_page(page)
    try:
        venue = p.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        venue = p.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        venue   = p.page(p.num_pages)
    return render(request, 'dashboard/blog-card.html', {'e':e, 'bi':bi, 'event':event, 'ev':ev, 'venue': venue,'inbox':receiver, 'rec_no': rec_no})

def blogdetail(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user.get_username())
        bi = member.objects.get(user=u)
        event = events.objects.all().order_by('-date')
        ev = events.objects.all().count()
        recipien = User.objects.get(username=request.user.get_username())
        receiver = Message.objects.filter(recipient=recipien)
        rec_no = Message.objects.filter(recipient=recipien).count()
        name = request.POST['name']
        e = events.objects.get(name=name)
        p = Paginator(events.objects.all().order_by('-date', '-time'), 6)
        page = request.GET.get('page')
        venue = p.get_page(page)
        try:
            venue = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            venue = p.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            venue = p.page(p.num_pages)
        return render(request, 'dashboard/blog-single-2.html', {'e': e,'bi':bi, 'event':event, 'ev':ev,'inbox':receiver,'rec_no': rec_no,'venue': venue})
    else:
        return redirect('ev')


def discussion(request):
    if request.method == 'POST':
        us = User.objects.get(username=request.user.get_username())
        bi = member.objects.get(user=us)
        event = events.objects.all().order_by('-date')
        ev = events.objects.all().count()
        recipien = User.objects.get(username=request.user.get_username())
        receiver = Message.objects.filter(recipient=recipien)
        name = request.POST['name']
        id = request.POST['heading']
        u = User.objects.get(username=name)
        e = thread.objects.get(user=u,id=id)
        er = replies.objects.filter(tread=e).count()
        co = replies.objects.filter(tread=e)
        rec_no = Message.objects.filter(recipient=recipien).count()
        p = Paginator(events.objects.all().order_by('-date', '-time'), 6)
        page = request.GET.get('page')
        venue = p.get_page(page)
        try:
            venue = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            venue = p.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            venue = p.page(p.num_pages)
        return render(request, 'dashboard/discussion.html',{'e':e, 'er':er, 'co':co,'bi':bi, 'event':event, 'ev':ev,'inbox':receiver,'rec_no': rec_no,'venue': venue})
    else:
        return redirect('threads')


def discussion_list(request):
    u = User.objects.get(username=request.user.get_username())
    bi = member.objects.get(user=u)
    event = events.objects.all().order_by('-date')
    ev = events.objects.all().count()
    recipien = User.objects.get(username=request.user.get_username())
    receiver = Message.objects.filter(recipient=recipien)
    rec_no = Message.objects.filter(recipient=recipien).count()
    dis = thread.objects.all().order_by('-date')
    sap = Paginator(thread.objects.all().order_by('-date'), 6)
    page= request.GET.get('page')
    q = sap.get_page(page)
    try:
        q = sap.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        q = sap.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        q = sap.page(sap.num_page)
    p = Paginator(events.objects.all().order_by('-date', '-time'), 6)
    page = request.GET.get('page')
    venue = p.get_page(page)
    try:
        venue = p.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        venue = p.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        venue = p.page(p.num_pages)
    return render(request, 'dashboard/discussion_list.html', {'dis':dis,'bi':bi, 'event':event, 'ev':ev, 'q': q, 'inbox':receiver,'rec_no': rec_no,'venue': venue})

def newcomment(request):
    if request.method == 'POST':
        comm = request.POST['comment']
        username = request.POST['name']
        duser = request.POST['discussionuser']
        heading = request.POST['heading']
        u = User.objects.get(username=duser)
        d = thread.objects.get(user=u,heading=heading)
        c = replies(user=username,tread=d,comment=comm)
        c.save()
        return redirect('threads')
    else:
        return redirect('threads')

def Question(request):
    if request.POST:
        print(request.POST)
        print('hello')
        date = datetime.datetime.now()
        print(request.FILES)
        heading = request.POST['heading']
        description = request.POST['description']
        img = request.FILES.get('image',None )
        if img != None:
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        else:
            img =''
        u = member.objects.get(user=request.user)
        d = thread.objects.create(user=u.user,date=date, heading=heading,description=description,image=img)
        return redirect('threads')
    else:
        us = User.objects.get(username=request.user.get_username())
        bi = member.objects.get(user=us)
        event = events.objects.all().order_by('-date')
        ev = events.objects.all().count()
        recipien = User.objects.get(username=request.user.get_username())
        receiver = Message.objects.filter(recipient=recipien)
        rec_no = Message.objects.filter(recipient=recipien).count()
        p = Paginator(events.objects.all().order_by('-date', '-time'), 6)
        page = request.GET.get('page')
        venue = p.get_page(page)
        try:
            venue = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            venue = p.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            venue = p.page(p.num_pages)
        return render(request,'dashboard/question.html',{'bi':bi, 'event':event, 'ev':ev, 'inbox':receiver,'rec_no': rec_no,'venue': venue})



