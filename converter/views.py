from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt

def handle_uploaded_file(file):
    return

def success(request):
    return HttpResponse("Successfully uploaded file")

def error(request):
    return HttpResponse("There was an error processing the file")

@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/converter/success')
        else:
            return HttpResponseRedirect('/converter/error')
    else:
        form = UploadFileForm()
    return render_to_response('converter/index.html', {'form': form})
