from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from forms import MessageForm
from zipfile import *
import shutil
import os
from os import listdir
from os.path import isfile, join
import qrcode

glob_id = 20

def API(request):
	s = ""
	if request.method == 'GET':
		resp = HttpResponse()
		resp.status_code = 200
		s+="<html>"
		s+="<body>"
		s+="<p style=\"text-align: center\">Gucci Gang</p>"
		s+="</body></html>"
		resp.write(s)
		return resp

	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

def mydevices(request):
	if request.method == 'GET':
		name = str(request.GET.get('name'))
	onlyfiles = [f for f in listdir('mytestsite/mytestsite/'+name) if isfile(join('mytestsite/mytestsite/'+name, f))]
	resp = HttpResponse()
	resp.status_code = 200
	for fl in onlyfiles:
		f = open('mytestsite/mytestsite/'+name + '/' +fl,'r')
		s = f.read().split('\n')
		resp.write(fl[:-4]+ ' ' + s[0] +' '+ s[2] + ' ')
	return resp

"""def newdevice(request):
	name = str(request.GET.get('name'))
	type1 = str(request.GET.get('type'))
	data = str(request.GET.get('data'))
	id1 = str(request.GET.get('id'))
	newfile
	return request"""
def add_device(request):
	name = str(request.GET.get('name'))
	id1 = str(request.GET.get('id'))
	shutil.move(r'mytestsite/mytestsite/unsorted/'+id1 + '.txt', r'mytestsite/mytestsite/'+name)
	print('mytestsite/mytestsite/unsorted/'+id1 + '.txt')
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

def reg(request):
	if request.method == 'GET':
		name = str(request.GET.get('name'))
		if not os.path.exists('mytestsite/mytestsite/' + name):
			os.makedirs('mytestsite/mytestsite/'+name)
	resp = HttpResponse()
	resp.status_code = 200
	resp.write('We need a request')
	return resp

def form(request):
	return render_to_response('form.html',{})

def qr(request):
	if request.method == 'GET':
		name = str(request.GET.get('name'))
		type1 = str(request.GET.get('type'))
		data = str(request.GET.get('data'))
		ip = str(request.GET.get('ip'))
		num = 0
		num  = int(request.GET.get('number'))
		for i in range(0,num):
			f = open('mytestsite/mytestsite/unsorted/'+name + str(i) + ".txt","w")
			f.write(type1 + '\n' + data + '\n' + ip)
			f.close()
		img = qrcode.make(name+str(i))
		img.save('mytestsite/mytestsite/static/active.png')
		zip = ZipFile('mytestsite/mytestsite/static/zip.zip',"w");
		for i in range(0,num):
			img = qrcode.make(name+str(i))
			img.save('mytestsite/mytestsite/static/'+ name+str(i)+'.png')
			zip.write('mytestsite/mytestsite/static/'+ name+ str(i) +'.png',name+str(i)+'.png')
			os.remove('mytestsite/mytestsite/static/'+ name+str(i)+'.png')
		zip.close()
		return render_to_response('qr.html', {})

	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp