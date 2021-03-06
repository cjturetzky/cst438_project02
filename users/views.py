from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
#not used since we inherited from userregosterform
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, RemoveUser
from .models import User

#user login decorator to show profile only if user is signed in
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def delete(request):
    print(request.user)
    if request.method == 'POST':
        print('if')
        form = RemoveUser(request.POST)
        if form.is_valid():
            
            password = form.cleaned_data.get('password')
            if User.objects.filter(username=request.user, password=password).exists():
                User.objects.filter(username=request.user).delete()
            else:
                print('wrong pass')
        else:
            print('not vaild')
  
    else:
        print('else')
        form = RemoveUser()
    return render(request, 'users/delete.html', {'form': form}) 


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error