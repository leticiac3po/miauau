from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from .models import *
from .evaluate import *
from django.conf import settings

# view for image submission
# saves the image, label and probability
def submit_img(request): 
    
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            
            # saves and organises information
            instance = form.save()
            instance.save()
            filepath = instance.image.path
            path = filepath.split('/')
            index = path.index('media')
            new_path = '/' + path[index] + '/' + path[index + 1] + '/' + path[index + 2]

            # evaluates using evaluate.py and saves results
            prob , instance.lbl = evaluate(filepath)
            instance.prob = str(round(float(prob), 4))
            instance.save()

            # passes the information to the result view
            request.session['path'] = new_path
            request.session['lbl'] = instance.lbl
            request.session['prob'] = instance.prob
            return redirect('result')
    else: 
        form = ImageForm() 
    return render(request, 'gato_ou_cachorro/image.html', {'form' : form}) 

# view that displays the image, label and probability
def result(request):

    path = request.session['path']
    lbl = request.session['lbl']
    prob = request.session['prob']
    return render(request, 'gato_ou_cachorro/result.html', {'path' : path, 'lbl' : lbl, 'prob' : prob})

# view that displays all past images and results
def gallery(request): 

    if request.method == 'GET': 
        Images = Image.objects.all()
        return render(request, 'gato_ou_cachorro/gallery.html', {'images' : Images}) 
