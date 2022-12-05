from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import logout


# Create log_out your views here.
def log_out(request):
    logout(request)
    return redirect('contracts:index')


# Create register your views here.
def register(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
