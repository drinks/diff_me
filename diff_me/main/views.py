from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from diff_me.main import models

def index(request):
    return render_to_response('index.html')

def show_by_slug_or_base58(request, id):
    diff = get_object_or_404(Diff, base58=id)
    diff.html = diff.diff_table()
    return render_to_response('diff.html', diff)