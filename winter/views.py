from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404,redirect
from .forms import UserForm
from .models import student,organization
# Create your views here.


def dashboard(request):
	return render(request, 'winter/dashboard.html', {})	


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'winter/dashboard.html', {'user':user})
            else:
                return render(request, 'winter/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'winter/login.html', {'error_message': 'Invalid login'})
    return render(request, 'winter/login.html')


def register_org(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                organization.user=request.user
                organization.org_name=request.user.username
                organization.save()
                return render(request, 'winter/dashboard_org.html', {'post':student.objects.all()})
    context = {
        "form": form,
    }
    return render(request, 'winter/register.html', context)


def register_stu(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        student.user=user
        student.student_name=username
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'winter/dashboard.html', {'user': user})
    context = {
        "form": form,
    }
    return render(request, 'winter/register.html', context)      

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'winter/login.html', context)      

def dash_stu(request):
	return render(request, 'winter/dashboard_stu.html', {'post':organization.objects.all()})
    	   	    

def dash_org(request):
	return render(request, 'winter/dashboard_org.html', {'post':student.objects.all()})	