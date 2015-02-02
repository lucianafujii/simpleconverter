from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .aws import policy, signature
from config import hosting_url, encoding_notify_url, encoding_notify_upload, encoding_notify_error
from encoding import transcode
import re

def handle_uploaded_file(file):
    return

def success(request):
    print 'bucket ' + request.GET['bucket']
    filename = re.sub (r'uploads/', '', request.GET['key'])
    print 'filename ' + filename
    transcode(filename,
            encoding_notify_url,
            encoding_notify_error,
            encoding_notify_upload)
    return HttpResponse("Successfully uploaded file " + filename)

def error(request):
    return HttpResponse("There was an error processing the file")

def index(request):
    return render_to_response('converter/index.html',
            {'policy': policy(), 'signature': signature(), 'url': hosting_url})


def encoding_uploaded(request):
    filename = request.GET['filename']
    return render_to_response('converter/play.html', {'filename': filename})
