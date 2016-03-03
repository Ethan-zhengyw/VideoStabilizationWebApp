from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from sift_SCIPY import stablilization
import os

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def upload(request):
    return render(request, 'upload.html')


def upload_video(request):
    base_dir = 'static/videos/'
    video_name = request.FILES['file'].name
    base_name = video_name[:video_name.rfind('.')]

    target_dir = os.path.join(base_dir, base_name)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    target = r'%s/%s' % (target_dir, video_name)

    with open(target, 'wb+') as destination:
        for chunk in request.FILES['file'].chunks():
            destination.write(chunk)

    stablilization.process(target)

    return HttpResponseRedirect('/')


def index(request):
    return HttpResponseRedirect('/home/')


def home(request):
    return render(request, 'home.html')


def download(request):
    videos = os.listdir('static/videos/')

    href_downloads = []
    for video in videos:
        href_download = {}

        href_download['href'] = 'static/videos/%s/result.mp4' % video
        contains = os.listdir('static/videos/%s' % video)
        for contain in contains:
            if 'result' not in contain and 'mp4' in contain:

                href_download['download'] = href_download['show'] = contain[:contain.rfind('.')]\
                                                                    + '_stabled' + contain[contain.rfind('.'):]
                href_download['href'] = '../' + href_download['href']

                href_downloads.append(href_download)


    print href_downloads

    return render(request, 'download.html', {
        'href_downloads': href_downloads
    })

