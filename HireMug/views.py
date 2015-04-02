from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from Job.models import job

# Create your views here.

def home(request):
	return render_to_response('home.html', {'jobs':job.objects.all()[::-1]} )
	
