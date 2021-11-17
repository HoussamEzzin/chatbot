from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} ! Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'users/register.html', context)