from django.shortcuts import render
from .forms import UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('documents_main')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'main/index.html')
@login_required
def contact(request):
    return render(request, 'main/contact.html')