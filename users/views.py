from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print('checkpoint')
        if form.is_valid():
            print('FORM IS VALID')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} ! Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method  == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'Information updated successfully !')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    return render(request, 'users/profile.html', context)
