from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Result, VerificationToken
from .forms import ResultForm, CustomUserCreationForm
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = CustomUserCreationForm(data)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email is verified
            user.save()
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)

            # Create verification token
            token = VerificationToken.objects.create(user=user)

            # Send verification email
            subject = 'Activate Your Account'
            html_message = render_to_string('emails/verification_email.html', {'user': user, 'token': token.token})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_email = user.email
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

            return JsonResponse({'message': 'Account created successfully. Please check your email for verification link.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/dashboard'})
            else:
                return JsonResponse({'errors': {'non_field_errors': ['Please verify your email to activate your account.']}}, status=400)
        else:
            return JsonResponse({'errors': {'non_field_errors': ['Invalid email or password']}}, status=400)
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Student').exists():
        results = Result.objects.filter(student=request.user)
        return render(request, 'dashboard/student_dashboard.html', {'results': results})
    elif request.user.groups.filter(name='Teacher').exists():
        results = Result.objects.all()
        form = ResultForm()
        return render(request, 'dashboard/teacher_dashboard.html', {'results': results, 'form': form})
    elif request.user.groups.filter(name='Admin').exists():
        return render(request, 'dashboard/admin_dashboard.html')
    else:
        return redirect('index')

@login_required
def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result added successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    return redirect('dashboard')

@login_required
def edit_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ResultForm(instance=result)
    return render(request, 'dashboard/edit_result.html', {'form': form, 'result': result})

@login_required
def delete_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        result.delete()
        messages.success(request, 'Result deleted successfully')
        return redirect('dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'result': result})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

def verify_email(request, token):
    try:
        verification_token = VerificationToken.objects.get(token=token)
        user = verification_token.user
        user.is_active = True
        user.save()
        verification_token.delete()
        messages.success(request, 'Your email has been verified. You can now log in.')
        return redirect('login')
    except VerificationToken.DoesNotExist:
        messages.error(request, 'Invalid verification token.')
        return redirect('register')

@login_required
def onboarding(request):
    return render(request, 'onboarding.html')

from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = CustomUserCreationForm(data)
        if form.is_valid():
            user = form.save()
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
            return JsonResponse({'message': 'Account created successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'redirect_url': '/dashboard'})
        else:
            return JsonResponse({'errors': {'non_field_errors': ['Invalid email or password']}}, status=400)
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Student').exists():
        results = Result.objects.filter(student=request.user)
        return render(request, 'dashboard/student_dashboard.html', {'results': results})
    elif request.user.groups.filter(name='Teacher').exists():
        results = Result.objects.all()
        form = ResultForm()
        return render(request, 'dashboard/teacher_dashboard.html', {'results': results, 'form': form})
    elif request.user.groups.filter(name='Admin').exists():
        return render(request, 'dashboard/admin_dashboard.html')
    else:
        return redirect('index')

@login_required
def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result added successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    return redirect('dashboard')

@login_required
def edit_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ResultForm(instance=result)
    return render(request, 'dashboard/edit_result.html', {'form': form, 'result': result})

@login_required
def delete_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        result.delete()
        messages.success(request, 'Result deleted successfully')
        return redirect('dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'result': result})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
