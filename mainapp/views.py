from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm
from .models import Query, Experiment
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
    results.build_query(organism=query.organism.replace(' ','').split(','), keywords=query.keywords.replace(' ','').split(','))
    results.search(keywords=query.keywords.replace(' ','').split(','),experiment=query.experiment_type.replace(' ','').split(','))
    results = results.get_results()
    for i in  results[0].iteritems():
        print i[0], i[1], 'xxx'
    results = [Experiment(source_query=query, experiment_id=i['accession'], experiment_type=i['experimenttype'], experiment_description=i['description'], experiment_link = 'https://www.ebi.ac.uk/arrayexpress/experiments/{}/'.format(i['accession'])) for i in results]
    for i in results:
        i.save()
    return render(request, 'results.html', {'result':results})
def _do_Sth(sth):
    return sth
