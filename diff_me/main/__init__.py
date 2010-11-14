from django.http import Http404
from django.shortcuts import get_object_or_404

def get_by_slug_or_base58(klass, id):
    try:
        obj = get_object_or_404(klass, slug=id)
    except Http404:
        obj = get_object_or_404(klass, base58=id)
    return obj