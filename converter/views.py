from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .aws import policy, signature
from config import hosting_url, encoding_notify_url, encoding_notify_upload, encoding_notify_error
from encoding import transcode
from converter.models import VideoFile
import json
import re

def handle_uploaded_file(file):
    return

def success(request):
    print 'bucket ' + request.GET['bucket']
    filename = re.sub (r'uploads/', '', request.GET['key'])
    print 'filename ' + filename
    response = transcode(filename,
            encoding_notify_url,
            encoding_notify_error,
            encoding_notify_upload)
    try:
        r = json.loads(response)
        media_id = r['response']['MediaID']
    except KeyError:
        return HttpResponse("Ocorreu um error processando o arquivo" + response)
    else:
        video_file = VideoFile(filename=filename, media_id=media_id, ready=False)
        video_file.save()
        return HttpResponse("O arquivo esta sendo processado: " + filename)

def error(request):
    return HttpResponse("There was an error processing the file")

def index(request):
    return render_to_response('converter/index.html',
            {'policy': policy(), 'signature': signature(), 'url': hosting_url})


def encoding_uploaded(request):
    filename = request.GET['filename']
    return render_to_response('converter/play.html', {'filename': filename})

@csrf_exempt
def notify_encoded(request):
    # Receives request from encoding when file is ready
    try:
        print request.POST['json']
    except KeyError:
        print "Couldn't get json response"
        return HttpResponse("OK")
    try:
        r = json.loads(request.POST['json'])
        media_id = r['result']['mediaid']
        print "media_id is " + media_id
    except KeyError:
        print "Problem receiving notify"
        return HttpResponse("OK")
    try:
        video_file = VideoFile.objects.get(media_id=media_id)
    except VideoFile.DoesNotExist:
        print "Problem getting the corresponding video file"
    else:
        video_file.ready = True
        video_file.save()
        print "file ready"
    return HttpResponse("OK")


