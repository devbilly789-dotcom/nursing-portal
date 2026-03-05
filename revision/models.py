from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
    COURSE_CHOICES = (
        ('BSN', 'BSN'),
        ('KRCHN', 'KRCHN'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    is_approved = models.BooleanField(default=False)
    mpesa_code = models.CharField(max_length=30, blank=True, null=True)
    stk_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Question(models.Model):
    COURSE_CHOICES = (
        ('BSN', 'BSN'),
        ('KRCHN', 'KRCHN'),
    )

    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    question_text = models.TextField()
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text[:50]
