from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from Job.models import job
from Job.forms import job_form

# Create your views here.

@login_required(login_url='/company_login')
def publish(request):

	if request.POST:
		form = job_form(request.POST)
		if form.is_valid():
			c = form.save(commit = False)
			c.user = request.user.username
			c.save()
			return HttpResponseRedirect('/company_profile')
	else:
		form = job_form()
		
	args = {}
	args.update(csrf(request))
	args['form'] = form		
	
	return render_to_response('job_publish.html',args)


@login_required(login_url='/company_login')
def detail(request,job_id):

	return render_to_response('job_detail.html', {'job':job.objects.get(id = job_id)} )


@login_required(login_url='/company_login')
def delete(request,job_id):
	job.objects.get(id = job_id).delete()
	return HttpResponseRedirect ('/company_profile')


