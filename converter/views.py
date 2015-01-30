from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .aws import policy, signature
from config import hosting_url

def handle_uploaded_file(file):
    return

def success(request):
    return HttpResponse("Successfully uploaded file")

def error(request):
    return HttpResponse("There was an error processing the file")

def index(request):
    return render_to_response('converter/index.html',
            {'policy': policy(), 'signature': signature(), 'url': hosting_url})

