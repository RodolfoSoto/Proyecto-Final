# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import UserManager
from django.contrib.auth.forms import AuthenticationForm 
from main.models import UserProfile
from main.forms import UserProfileForm, CreationForm, TweeetForm, EditForm


def home(request):
	form = AuthenticationForm()	
	#if request.method == 'POST':
	if request.method == 'POST':
		form = AuthenticationForm(None, request.POST)
		if form.is_valid():
			auth.login(request, form.get_user())		
			return redirect('tweet')	
	return render_to_response('home.html', {
		'form' : form,
	}, RequestContext(request))

#pull, add, commit, push

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



#def edit_article(request, pk):
#	article = get_object_or_404(Article, pk=pk)
#	form = ArticleForm(instance=article)
#	if request.method =='POST':
#		form = ArticleForm(request.POST, instance=article)
#		if form.is_valid():
#			form.save()
#		return redirect('home')
#	return render_to_response('add_article.html',{
#		'form': form,
#	}, RequestContext(request))

#def show_article(request, pk):
#	article = get_object_or_404(Article, pk=pk)
#	return render_to_response('show_article.html', {
#		'article': article,
#	})

	
