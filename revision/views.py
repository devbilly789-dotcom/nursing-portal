from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import StudentProfile, Question


# ==========================
# REGISTER VIEW
# ==========================
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        course = request.POST.get('course')

        if form.is_valid():
            user = form.save()

            # Create profile for the new user
            StudentProfile.objects.create(
                user=user,
                course=course
            )

            login(request, user)
            return redirect('payment')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# ==========================
# PAYMENT VIEW
# ==========================
@login_required
def payment_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    # If already approved, go to dashboard
    if profile.is_approved:
        return redirect('dashboard')

    if request.method == "POST":
        mpesa_code = request.POST.get('mpesa_code')
        profile.mpesa_code = mpesa_code
        profile.save()
        return redirect('waiting')

    return render(request, 'payment.html')


# ==========================
# WAITING VIEW
# ==========================
@login_required
def waiting_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    # If approved, go to dashboard
    if profile.is_approved:
        return redirect('dashboard')

    return render(request, 'waiting.html')


# ==========================
# DASHBOARD VIEW (Questions)
# ==========================
@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    # If no payment submitted
    if not profile.mpesa_code:
        return redirect('payment')

    # If not approved yet
    if not profile.is_approved:
        return redirect('waiting')

    # Show questions based on course
    questions = Question.objects.filter(course=profile.course)

    return render(request, 'questions.html', {
        'questions': questions
    })


# ==========================
# ADMIN APPROVAL VIEW
# ==========================
@staff_member_required
def approve_students(request):
    students = StudentProfile.objects.filter(
        is_approved=False,
        mpesa_code__isnull=False
    )

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = StudentProfile.objects.get(id=student_id)
        student.is_approved = True
        student.save()

        return redirect('approve_students')

    return render(request, 'approve_students.html', {
        'students': students
    })
