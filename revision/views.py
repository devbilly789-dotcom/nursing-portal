from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudentProfile, Question


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        course = request.POST.get('course')

        if form.is_valid():
            user = form.save()
            profile = StudentProfile.objects.get(user=user)
            profile.course = course
            profile.save()
            login(request, user)
            return redirect('payment')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def payment_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    # If user is already approved, redirect to dashboard
    if profile.is_approved:
        return redirect('dashboard')

    # Handle MPESA submission
    if request.method == "POST":
        mpesa_code = request.POST.get('mpesa_code')
        profile.mpesa_code = mpesa_code
        profile.save()

    # Check if user submitted MPESA code but is still waiting for approval
    waiting = False
    if profile.mpesa_code and not profile.is_approved:
        waiting = True

    return render(request, 'payment.html', {'waiting': waiting})


@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    # If not approved yet, redirect to payment page
    if not profile.is_approved:
        return redirect('payment')

    questions = Question.objects.filter(course=profile.course)
    return render(request, 'questions.html', {'questions': questions})