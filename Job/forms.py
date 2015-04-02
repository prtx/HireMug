from django import forms
from models import job

class job_form(forms.ModelForm):
	
	class Meta:
		model = job
		fields = ('title','description',)
		get_latest_by = 'date'


