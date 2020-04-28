from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class BooksSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_url = 'profile_edit.html'

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

class CreateProfile(CreateView):
    form_class = UserEditForm, ProfileEditForm
    template_name = 'profile_edit.html'

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('bookslist_url')
        else:
            form = ProfileEditForm
            return render(request, 'profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                    'profile_edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})