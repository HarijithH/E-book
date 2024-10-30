from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "Admin login.html")


def user_feedback(request):
    return render(request, "View User Feedback.html")


def view_complaint(request):
    return render(request, "View complaint.html")


def send_reply(request):
    return render(request, "send reply.html")


def view_history(request):
    return render(request, "View History.html")


def admin_home(request):
    return render(request, "admin home.html")