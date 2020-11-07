from django.shortcuts import render, HttpResponse, Http404
from demoapp.models import Movie
from django.forms.models import model_to_dict
import json

# Create your views here.
def home(request):
    raw_data = Movie.objects.raw_list_data()
    return render(request, "home.html", {'raw_data': raw_data})

def details(request, pk):
    raw_detail = Movie.objects.raw_details(pk)
    if not raw_detail:
        raise Http404('contact with Techniqual support')
    return render(request, "details.html", {'raw_detail':raw_detail})

def autocompleteModel(request):
    q = request.GET.get('query', '')
    search_qs = Movie.objects.ajax_name(q)
    results = []
    for r in search_qs:
        result_dict = r.__dict__
        result_dict.pop('_state', '')
        results.append(result_dict)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)