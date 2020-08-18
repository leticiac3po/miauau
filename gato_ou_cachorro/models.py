from django.db import models

# model for the image, with the label and probability
class Image(models.Model):
	image = models.ImageField(upload_to = 'images/', db_column = 'img')
	lbl = models.CharField(max_length = 20, default = 'error')
	prob = models.CharField(max_length = 20, default = '-1')

	def __str__(self):
		return self.lbl

