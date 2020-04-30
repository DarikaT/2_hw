from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView
from .models import Profile
from books.models import Books
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class UserSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['books'] = Books.objects.filter()
        return context     
  
    
@login_required
def edit(request, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('profile_url', args=[request.user.pk])) 
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
