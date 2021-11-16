from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'users/regsiter.html', context)