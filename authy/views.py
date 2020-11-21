from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from authy.forms import SignupForm , EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user.refresh_from_db()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.set_password(password)
			user.save()
			
			
			user = authenticate(username=user.username, password=password)
		
			return redirect('authy:login')
	else:
		form = SignupForm()

	context = {
		'form': form,
	}

	return render(request, 'registration/signup.html', context)



@login_required
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')
			profile.location = form.cleaned_data.get('location')
			profile.url = form.cleaned_data.get('url')
			profile.profile_info = form.cleaned_data.get('profile_info')
			profile.save()
			return redirect('index')
	else:
		form = EditProfileForm()

	context = {
		'form': form,
	}

	return render(request, 'edit_profile.html', context)


class PasswordChange(PasswordChangeView):
	success_url = reverse_lazy('authy:password_change_done')