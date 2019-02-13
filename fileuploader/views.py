from random import randint

from project import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage

from PIL import Image
import glob, os

def index(request):
    return render(request, 'fileuploader/index.html')


def upload(request):
    photo_url = default_storage.save('file.jpg', request.FILES['fileToUpload'])
    context = {'image' : photo_url}
    request.session['Url'] = photo_url;
    return render(request, 'fileuploader/editor.html', context)


def new_photo(request):
	return redirect("/")


def share(request):
	path = settings.MEDIA_ROOT
	edited_photos = os.listdir(path)
	context = {'edited_photos' : edited_photos}
	return render(request, 'fileuploader/share.html', context)


def crop(request):
	try :
		request.session['Url']
		img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
		img_edited = img.crop((int(request.POST.get('upper_left')), int(request.POST.get('lower_left')), int(request.POST.get('upper_right')), int(request.POST.get('lower_right'))))
		img_edited.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
		context = {'image' : request.session['Url']}
		return render(request, 'fileuploader/editor.html', context)
	except :
		return HttpResponse ('crop Error :(')



def resize(request):
	try :
		img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))	
		img_edited = img.resize((int(request.POST.get('width')), int(request.POST.get('height'))))
		img_edited.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
		context = {'image' : request.session['Url']}
		return render(request, 'fileuploader/editor.html', context)
	except :
		return HttpResponse ('resize Error :(')



def rotate(request):
	img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
	img_edited = img.rotate(int(request.POST.get('degree')), expand = 1)
	img_edited.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
	context = {'image' : request.session['Url']}
	return render(request, 'fileuploader/editor.html', context)


def black_white(request):
	img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
	img_edited = img.convert("L")
	img_edited.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
	context = {'image' : request.session['Url']}
	return render(request, 'fileuploader/editor.html' , context)
