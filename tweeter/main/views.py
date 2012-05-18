# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import UserManager
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm 
from main.models import UserProfile, Tweeet
from main.forms import UserProfileForm, CreationForm, TweeetForm, EditForm


def home(request):
	form = AuthenticationForm()	
	if request.method == 'POST':
		form = AuthenticationForm(None, request.POST)
		if form.is_valid():
			auth.login(request, form.get_user())		
			return redirect('tweet')	
	return render_to_response('home.html', {
		'form' : form,
	}, RequestContext(request))


def Main(request, pk):    
	pass


def register(request):
	form = CreationForm()
	if request.method == 'POST':
		form=CreationForm(request.POST)
		if form.is_valid():
			user = form.save()			
			UserProfile.objects.create(author=user)
			return redirect('home')
	return render_to_response('register.html', {
		'form': form,
 		}, RequestContext(request))


def tweet(request):
	form = TweeetForm()
	users = UserProfile.objects.all()
	puser = get_object_or_404(UserProfile, author=request.user)
	if request.method == 'POST':
		form= TweeetForm(request.POST)		
		if form.is_valid():
			tweet = form.save(commit = False)
			user = get_object_or_404(UserProfile, author=request.user)
			tweet.author = user
			tweet = form.save()
			return redirect('tweet')
	return render_to_response('tweet.html', {
		'form': form,
		'users': users,
		'puser': puser,
		}, RequestContext(request))


def delete_tweet(request,pk):
	Tweeet.objects.filter(pk=pk).delete()
	return redirect('tweet')


def edit_tweet(request, pk):
	tweet = get_object_or_404(Tweeet, pk=pk)
	form = TweeetForm(instance=tweet)
	if request.method =='POST':
		form = TweeetForm(request.POST, instance=tweet)
		if form.is_valid():
			form.save()
		return redirect('tweet')
	return render_to_response('edit_tweet.html',{
		'form': form,
	}, RequestContext(request))


def edit(request):
	profile = get_object_or_404(UserProfile, author=request.user)
	form = EditForm()
	form2 = UserProfileForm(instance=profile)
	if request.method == 'POST':
		form = EditForm(request.POST,instance=profile)
		if form.is_valid():
			form.save()						
		return redirect('tweet')
	return render_to_response('edit.html',{
		'form': form,
	}, RequestContext(request))


def follows(request,pk):
	pass	


def logout_view(request):
	logout(request)
	return redirect('home')
	
	
def password_reset(request):
	form= PasswordResetForm()
	if request.method == 'POST':
		form=PasswordResetForm(request.POST)
		if form.is_valid():
			return redirect('home')
	return render_to_response('password_reset_form.html',{
		'form': form,
	}, RequestContext(request))
