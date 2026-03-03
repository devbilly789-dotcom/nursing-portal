from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import StudentProfile, Question


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        course = request.POST.get('course')

        if form.is_valid():
            user = form.save()

            # FIX: Avoid UNIQUE constraint error
            StudentProfile.objects.get_or_create(
                user=user,
                defaults={'course': course}
            )

            login(request, user)
            return redirect('payment')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def payment_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "POST":
        mpesa_code = request.POST.get('mpesa_code')
        profile.mpesa_code = mpesa_code
        profile.save()
        return redirect('waiting')  # redirect to waiting page after submitting code

    return render(request, 'payment.html')


@login_required
def waiting_view(request):
    """
    Page shown after student submits MPESA code,
    waiting for admin approval
    """
    return render(request, 'waiting.html')


@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    if not profile.is_approved:
        # Redirect to waiting if not approved
        return redirect('waiting')

    questions = Question.objects.filter(course=profile.course)
    return render(request, 'questions.html', {'questions': questions})


# Only admin/staff can approve students
@user_passes_test(lambda u: u.is_staff)
def approve_students(request):
    students = StudentProfile.objects.filter(is_approved=False, mpesa_code__isnull=False)

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = StudentProfile.objects.get(id=student_id)
        student.is_approved = True
        student.save()

    return render(request, 'approve_students.html', {'students': students})
