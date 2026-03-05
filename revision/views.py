from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
import json
=======
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import StudentProfile, Question
>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6

from .models import StudentProfile, Question
from .payhero import PayHeroSTK

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        course = request.POST.get('course')

        if form.is_valid():
            user = form.save()
<<<<<<< HEAD
            StudentProfile.objects.create(user=user, course=course)
=======

            # FIX: Avoid UNIQUE constraint error
            StudentProfile.objects.get_or_create(
                user=user,
                defaults={'course': course}
            )

>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6
            login(request, user)
            return redirect('payment')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

<<<<<<< HEAD
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
=======

@login_required
def payment_view(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "POST":
        mpesa_code = request.POST.get('mpesa_code')
        profile.mpesa_code = mpesa_code
        profile.save()
        return redirect('waiting')  # redirect to waiting page after submitting code
>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6

        payhero = PayHeroSTK(settings.PAYHERO_CONFIG)
        result = payhero.initiate_stk_push(phone_number, amount, reference, customer_name=request.user.username)

        if result and result.get("success"):
            profile.stk_reference = result.get("reference")
            profile.save()
            return redirect('waiting')
        else:
            context = {"error": "Failed to initiate payment. Please try again."}
            return render(request, "payment.html", context)

    return render(request, "payment.html")

@login_required
def waiting_view(request):
<<<<<<< HEAD
    profile = StudentProfile.objects.get(user=request.user)
    if profile.is_approved:
        return redirect('dashboard')
    return render(request, "waiting.html")

# ==========================
# DASHBOARD VIEW
# ==========================
@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)
    if not profile.mpesa_code:
        return redirect('payment')
=======
    """
    Page shown after student submits MPESA code,
    waiting for admin approval
    """
    return render(request, 'waiting.html')


@login_required
def dashboard_view(request):
    profile = StudentProfile.objects.get(user=request.user)

>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6
    if not profile.is_approved:
        # Redirect to waiting if not approved
        return redirect('waiting')

    questions = Question.objects.filter(course=profile.course)
    return render(request, 'questions.html', {'questions': questions})
<<<<<<< HEAD
=======

>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6

# Only admin/staff can approve students
@user_passes_test(lambda u: u.is_staff)
def approve_students(request):
    students = StudentProfile.objects.filter(is_approved=False, mpesa_code__isnull=False)
<<<<<<< HEAD
=======

>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = StudentProfile.objects.get(id=student_id)
        student.is_approved = True
        student.save()
<<<<<<< HEAD
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
=======

    return render(request, 'approve_students.html', {'students': students})
>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6
