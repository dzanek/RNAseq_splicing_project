from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm
from .models import Query, Sample
import random as r
import string
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
    query = query._to_list()
    return render(request, 'results.html', {'result':list(query)})
def _do_Sth(sth):
    return sth
