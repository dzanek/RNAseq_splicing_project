from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm
from .models import Query, Sample
import random as r
import string

from array_express_api import *

# Create your views here.

def home(request):
    ''' '''
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.query_id = ''.join([r.choice(string.ascii_letters + string.digits) for i in range(6)])
            query.save()
            return redirect('search_results', query_id = query.query_id)
    else:
        form = QueryForm()
    return render(request,'index.html', {'form':form})

def search_results(request, query_id):
    ''' '''
    query = get_object_or_404(Query, query_id = query_id)
    results = Array_express()
    results.build_query(organism=query.organism.split(','), keywords=query.keywords.split(','))
    results.search(keywords=query.keywords.split(','),experiment=query.experiment_type.split(','))
    results = results.get_results()
    results = [str(i) for i in results]

    return render(request, 'results.html', {'result':results})
def _do_Sth(sth):
    return sth
