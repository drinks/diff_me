from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from diff_me.main import get_by_slug_or_base58
from diff_me.main.models import Diff, DiffForm

def index(request):
    form = DiffForm()
    return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))

def create(request):
    data = request.POST.copy()
    form = DiffForm(data)
    errors = form.errors
    
    if not errors:
        diff = Diff(**form.cleaned_data)
        diff.save()
        return redirect(diff_html, id=diff.base58)
    else:
        render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))

def edit(request, id):
    pass

def diff_html(request, id):
    data = get_by_slug_or_base58(Diff, id)
    return render_to_response('diff.html', {'diff': data})

def diff_raw(request, id):
    data = get_by_slug_or_base58(Diff, id)
    return HttpResponse(data.diff_unified_str(), mimetype="text/plain")
