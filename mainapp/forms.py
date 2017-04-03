from django import forms
from .models import Query

class QueryForm(forms.ModelForm):
    ''' '''
    class Meta:
        ''' '''
        model = Query
        fields = ('keywords', 'organism', 'experiment_type')
