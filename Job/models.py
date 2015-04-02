from django.db import models

# Create your models here.

class job(models.Model):
	
	title = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True, editable=False)
	
	def __unicode__(self):
		return self.id()
