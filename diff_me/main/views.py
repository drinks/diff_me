from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from diff_me.main import models

def index(request):
    return render_to_response('index.html')