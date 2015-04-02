from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

from forms import company_form, update_form
from Job.models import job

# Create your views here.


def register(request):
	
	if request.method=='POST':
		form = company_form(request.POST)
		if form.is_valid():
			form.save()
			request.session['user'] = request.POST.get('name')
			return HttpResponseRedirect('/company_profile')
	else:
		form = company_form()
	
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('company_register.html',args)

	
def login(request):

	args = {} # c is the name of dict file
	args.update(csrf(request))
	args['message'] = ''
	
	username = request.POST.get('username',None)
	password = request.POST.get('password',None)
	
	user = auth.authenticate(username=username, password=password)
	print user
	
	if user:
		auth.login(request,user)
		#user.is_active = True
		request.session.set_expiry(600)
		return HttpResponseRedirect('/company_profile')
	else:
		if username:
			args['message'] = 'Sorry, Invalid'
	
	return render_to_response('company_login.html',args)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):

	if request.user == AnonymousUser():
			return HttpResponseRedirect('/company_login')
	
	return render_to_response('company_profile.html', 
		{
		'user':request.user.username, 
		'jobs':job.objects.filter(user=request.user.username)[::-1]
		}
	)
	
	'''return render_to_response('user.html',{
			'asg2': asgmnt1.objects.filter(assignment = True).order_by('doi'),		
			'date1' :date.today(),
			'ramailo': newuser.objects.filter(user = request.user),
			'full_name' : request.user.username,
			'comments2':comment.objects.all().order_by('-pub_date'),
	 		'status2' : status1.objects.all().order_by('-syear')}
	)# might be wrong'''


@login_required(login_url='/company_login')
def update(request):
	
	if request.user == AnonymousUser():
			return HttpResponseRedirect('/company_login')
	
	if request.POST:
		form = update_form(request.POST,request.FILES,instance=request.user.profile)
		if form.is_valid():
			a = form.save(commit = False)
			a.save()
			return HttpResponseRedirect('/company_profile')
	else:
		user = request.user
		profile = user.profile
		form  = update_form(instance = profile)
		
	args = {}
	args.update(csrf(request))
	args['form'] = form
		
	return render_to_response('company_update.html',args)
	
	
@cache_control(no_cache=True, must_revalidate=True, no_store=True)	
def logout(request):
	
	if hasattr(request, 'user'):
	     	request.user = AnonymousUser()
	
	auth.logout(request)
	request.session.flush()
	
	return HttpResponseRedirect('/')

