from django.shortcuts import render , redirect , get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from authy.forms import SignupForm , EditProfileForm , EditProfileUserForm
from authy.models import Profile
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
			user.profile.email = form.cleaned_data.get('email')
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
	user_instance = User.objects.get(id=user)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES,instance=request.user)
		userprofile_form = EditProfileUserForm(request.POST,instance=request.user.profile)
		if form.is_valid() and userprofile_form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			# user_instance.first_name = userprofile_form.cleaned_data.get('first_name')
			user_instance.profile.first_name = userprofile_form.cleaned_data.get('first_name')
			user_instance.profile.last_name = userprofile_form.cleaned_data.get('last_name')
			user_instance.email = userprofile_form.cleaned_data.get('email')
			profile.location = form.cleaned_data.get('location')
			profile.url = form.cleaned_data.get('url')
			profile.profile_info = form.cleaned_data.get('profile_info')
			profile.save()
			user_instance.save()
			return redirect('index')
	else:
		form = EditProfileForm(instance=profile)
		userprofile_form = EditProfileUserForm(instance=user_instance)

	context = {
		'form': form,
		'userprofile_form':userprofile_form,
	}

	return render(request, 'edit_profile.html', context)


class PasswordChange(PasswordChangeView):
	success_url = reverse_lazy('authy:password_change_done')


def UserProfile(request,username):
	user = get_object_or_404(User,username=username)
	profile = Profile.objects.get(user=user)

	context={
		'profile':profile
	}
	template = loader.get_template('profile.html')

	return HttpResponse(template.render(context,request))
	