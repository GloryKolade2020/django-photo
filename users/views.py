from django.shortcuts import render,redirect

from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(("gallery"))