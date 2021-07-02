from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .models import Admin,member
from dashboard.models import events
from postman.models import Message
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None and member.objects.get(user=user):
            auth.login(request,user)
            return redirect('Userdashboard')
        elif user is not None and Admin.objects.get(user=user):
            auth.login(request, user)
            return redirect('Admindashboard')
        else:
            return render(request, 'accounts/Signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'accounts/Signin.html')

def Userdashboard(request):
    u = User.objects.get(username=request.user.get_username())
    sub = member.objects.get(user=u)
    bi = member.objects.get(user=u)
    recipien = User.objects.get(username=request.user.get_username())
    receiver = Message.objects.filter(recipient=recipien)
    rec_no = Message.objects.filter(recipient=recipien).count()
    event = events.objects.all().order_by('-date')
    ev = events.objects.all().count()
    e = events.objects.all().order_by('-date')
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
    return render(request, 'accounts/user-profile.html', {'sub': sub, 'bi': bi, 'event': event, 'ev': ev, 'inbox': receiver,'rec_no': rec_no,'venue': venue, 'e':e})


def Admindashboard(request):
    u = User.objects.get(username=request.user.get_username())
    sub = Admin.objects.get(user=u)
    bi = member.objects.all()

    return render(request, 'accounts/instructorprofile.html', {'sub': sub, 'bi': bi})


def updatebio(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        u = User.objects.get(username=request.user.get_username())
        member.objects.filter(user=u).update(firstname=fname, secondname=sname)
        mg = 'bio updated!'
        sub = member.objects.get(user=u)
        bi = member.objects.get(user=u)
        recipien = User.objects.get(username=request.user.get_username())
        receiver = Message.objects.filter(recipient=recipien)
        rec_no = Message.objects.filter(recipient=recipien).count()
        ev = events.objects.all().count()
        event = events.objects.all().order_by('-date')
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
        return render(request,'accounts/edit-userprofile.html', {'mg': mg,'sub': sub, 'bi': bi,'rec_no': rec_no,'ev': ev,'event': event,'inbox': receiver,'venue': venue})
    else:
        u = User.objects.get(username=request.user.get_username())
        bi = member.objects.get(user=u)
        sub = member.objects.get(user=u)
        recipien = User.objects.get(username=request.user.get_username())
        receiver = Message.objects.filter(recipient=recipien)
        rec_no = Message.objects.filter(recipient=recipien).count()
        ev = events.objects.all().count()
        event = events.objects.all().order_by('-date')
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
        return render(request,'accounts/edit-userprofile.html', {'bi': bi,'sub': sub, 'bi': bi,'rec_no': rec_no,'ev': ev,'event': event,'inbox': receiver,'venue': venue})


def updateimage(request):
    if request.method == 'POST' and request.FILES['img']:
        img = request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
        v = request.user.get_username()
        f = User.objects.get(username=v)
        member.objects.filter(user=f).update(image=file)
        u = User.objects.get(username=request.user.get_username())
        bi = member.objects.get(user=u)
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
        return render(request, 'accounts/edit-userprofile.html', {'bi': bi,'venue': venue})
    else:
        u = User.objects.get(username=request.user.get_username())
        su = member.objects.get(user=u)
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
        return render(request,'accounts/edit-userprofile.html', {'su':su,'venue': venue})


def signup(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['password']
        mat = request.POST['matno']
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            u = User.objects.get(username=email)
            fname = request.POST['fname']
            sname = request.POST['sname']
            su = member(user=u,firstname=fname,secondname=sname,matno=mat)
            su.save()
            return redirect('signin')
        else:
            mg = 'passwords must match'
            return render(request, 'accounts/Signup.html', {'mg': mg})
    else:
        return render(request, 'accounts/Signup.html')

def redr(request):
    return redirect(reverse('ev'))