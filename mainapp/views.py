from django.shortcuts import render, redirect
from .forms import QueryForm
# Create your views here.

def home(request):
    ''' '''
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save()
            #post.save()
            return redirect('search_results', terms = query)
    else:
        form = QueryForm()
    return render(request,'index.html', {'form':form})

def search_results(request, terms):
    ''' '''
    results = _do_Sth(terms)
    return render(request, 'results.html', {'results':results})
def _do_Sth(sth):
    return sth
