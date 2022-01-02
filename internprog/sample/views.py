from django.shortcuts import render
from .models import FilesAdmin
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import os
import json
def index(request):
    return render(request,'abcd2.html')
def anmol(request):
    font = ImageFont.truetype('arial.ttf',180)
    li=[]
    inst_name="XYZ Institute"
    if request.method=='POST':
        stri=request.POST["name"]
        li = stri.split(',');
        if len(li)>0:
            for i in li:
                try:
                    if len(i)>3:
                        instance=FilesAdmin(title=i)
                        instance.save()
                        img = Image.open('C:/abcd/internprog/image_certificate/cert.jpg')
                        draw = ImageDraw.Draw(img)
                        draw.text(xy=(4500,3300),text='{}'.format(i),fill=(0,0,0),font=font)
                        draw.text(xy=(7050,4800),text='{}'.format(inst_name),fill=(0,0,0),font=font)
                        img.save('media_cdn/media/{}.jpg'.format(i))
                except:
                    print("an error occured")
        else:
            li=[]
    context={'file':FilesAdmin.objects.filter(title__in=li)}
    return render(request,'abcd.html',context)
def download():
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
