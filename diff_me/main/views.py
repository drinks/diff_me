from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
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
        return redirect(diff_html, base58=diff.base58)
    else:
        return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))

def edit(request, base58=None):
    diff = Diff.objects.get(base58=base58)
    form = DiffForm(instance=diff)

    if request.POST:
        data = request.POST.copy()
        form = DiffForm(data)
        errors = form.errors
        if not errors:
            new_diff = Diff(**form.cleaned_data)
            new_diff.parent = diff.parent or diff.pk
            new_diff.save()
            return redirect(diff_html, base58=new_diff.base58)
        else:
            return render_to_response('edit.html', {'form': form, 'diff': diff}, context_instance=RequestContext(request))        
    
    return render_to_response('edit.html', {'form': form, 'diff': diff}, context_instance=RequestContext(request))

def diff_html(request, base58=None):
    data = Diff.objects.get(base58=base58)
    return render_to_response('diff.html', {'diff': data})

def diff_raw(request, base58=None, type='txt'):
    mime = 'plain' if type=='txt' else type
    data = Diff.objects.get(base58=base58)
    return HttpResponse(data.diff_unified_str(), mimetype='text/%s' % mime)
