from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
import json

from .models import StudentProfile, Question
from .payhero import PayHeroSTK

# ==========================
# REGISTER VIEW
# ==========================
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        course = request.POST.get('course')

        if form.is_valid():
            user = form.save()

            # Avoid UNIQUE constraint error
            StudentProfile.objects.get_or_create(
                user=user,
                defaults={'course': course}
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

    if profile.is_approved:
        return redirect('dashboard')

    if request.method == "POST":
        phone_number = request.POST.get("phone")
        amount = 500  # Example fee
        reference = "PYT_" + datetime.now().strftime("%Y%m%d%H%M%S")

        payhero = PayHeroSTK(settings.PAYHERO_CONFIG)
        result = payhero.initiate_stk_push(
            phone_number, amount, reference, customer_name=request.user.username
        )

        if result and result.get("success"):
            profile.stk_reference = result.get("reference")
            profile.save()
            return redirect('waiting')
        else:
            context = {"error": "Failed to initiate payment. Please try again."}
            return render(request, "payment.html", context)

    return render(request, "payment.html")

# ==========================
# WAITING VIEW
# ==========================
@login_required
def waiting_view(request):
    """
    Page shown after student submits MPESA code,
    waiting for admin approval
    """
    return render(request, 'waiting.html')

# ==========================
# DASHBOARD VIEW
# ==========================
@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    if not profile.is_approved:
        # Redirect to waiting if not approved
        return redirect('waiting')

    questions = Question.objects.filter(course=profile.course)
    return render(request, 'questions.html', {'questions': questions})

# ==========================
# ADMIN APPROVE STUDENTS VIEW
# ==========================
@user_passes_test(lambda u: u.is_staff)
def approve_students(request):
    students = StudentProfile.objects.filter(is_approved=False, mpesa_code__isnull=False)

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = StudentProfile.objects.get(id=student_id)
        student.is_approved = True
        student.save()
        return redirect('approve_students')

    return render(request, 'approve_students.html', {'students': students})

# ==========================
# PAYHERO CALLBACK VIEW
# ==========================
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payhero_callback(request):
    data = json.loads(request.body)
    reference = data.get("external_reference")
    status = data.get("status")

    try:
        profile = StudentProfile.objects.get(stk_reference=reference)
        if status == "SUCCESS":
            profile.mpesa_code = data.get("provider_reference")
            profile.is_approved = True
            profile.save()
        return JsonResponse({"status": "received"})
    except StudentProfile.DoesNotExist:
        return JsonResponse({"status": "not_found"}, status=404)
