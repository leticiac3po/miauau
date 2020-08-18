from django import forms
from .models import *

# form to get the submitted image
class ImageForm(forms.ModelForm):

	class Meta:
		model = Image
		fields = ['image']