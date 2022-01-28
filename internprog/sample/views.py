from django.shortcuts import render
from .models import FilesAdmin
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from PIL import Image, ImageDraw, ImageFont
import os
import json
from json import dumps
def loginuser(request):
	if request.user.is_authenticated:
			user=request.user
			cont = FilesAdmin.objects.filter(user=user)
			li = []
			for ins in cont:
				li.append(ins.title)
			li = dumps(li)
			context = {'li': li}
			return render(request, 'index.html', context)
	else:
		if request.method=="POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				cont = FilesAdmin.objects.filter(user=user)
				li = []
				for ins in cont:
					li.append(ins.title)
				li = dumps(li)
				context = {'li': li}
				return render(request, 'index.html', context)
			else:
				messages.add_message(request,messages.INFO,'invalid credentials')
				return render(request, 'login.html')

		else:
			messages.add_message(request,messages.INFO,'invalid credentials')
			return render(request, 'login.html')
		# Return an 'invalid login' error message.
		...


def index(request):

	return render(request, 'login.html')


def anmol(request):
	font = ImageFont.truetype('arial.ttf', 180)
	li = []
	inst_name = "XYZ Institute"
	if request.method == 'POST':
		stri = request.POST["name"]
		li = stri.split(',')
		if len(li) > 0:
			for i in li:
				try:
					if len(i) > 3:
						instance = FilesAdmin(title=i)
						instance.save()
						img = Image.open(
							'C:/abcd/internprog/image_certificate/cert.jpg')
						draw = ImageDraw.Draw(img)
						draw.text(xy=(4500, 3300), text='{}'.format(
							i), fill=(0, 0, 0), font=font)
						draw.text(xy=(7050, 4800), text='{}'.format(
							inst_name), fill=(0, 0, 0), font=font)
						img.save('media_cdn/media/{}.jpg'.format(i))
				except:
					print("an error occured")
		else:
			li = []
	context = {'file': FilesAdmin.objects.filter(title__in=li)}
	return render(request, 'abcd.html', context)
def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request,"index.html")
	# if not GET, then proceed
	li=[]
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			return redirect('/home', foo='bar')
		#if file is too large, return
		if csv_file.multiple_chunks():
			return render(request, "index.html")

		file_data = csv_file.read().decode("utf-8")		

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:	
			try:					
			    fields = line.split(",")
			    li.append(fields[0])
			except Exception as e:
				print("ug")
			# try:
			# 	form = EventsForm(data_dict)
			# 	if form.is_valid():
			# 		form.save()					
			# 	else:
			# 		logging.getLogger("error_logger").error(form.errors.as_json())												
			# except Exception as e:
			# 	logging.getLogger("error_logger").error(repr(e))					
			# 	pass

	except Exception as e:
		return redirect('/home', foo='bar')

	context={'li':dumps(li)}
	print(li)
	return render(request, "index2.html",context)