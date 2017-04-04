'''Module for programmatic access to array express
Uses API with json as interface between AE and python
'''

import urllib2 as url
import json
import sys

class Array_express:
    ''' '''
    base_url = 'https://www.ebi.ac.uk/arrayexpress/json/v3/experiments'

    def __init__(self):
        ''' '''
        pass

    def build_query(self,organism=[],experiment=[]):
        ''' '''
        self.query = self.base_url+'?organism={}&keywords={}'.format('+'.join(organism),'+'.join(experiment))
        print self.query
    def _any_has_any(self, queries, items):
        ''' checks if any from queries is in any of items '''
        return [item for item in items if len([term for term in queries if term in str(item)]) > 0]

    def _parse_json(self,json_text,keywords=[], experiment=[]):
        ''' Takes text json object, returns list of experiments that matches terms '''
        loaded_json = json.loads(json_text)
        print loaded_json['experiments']
        if loaded_json['experiments']['total'] == 0:
            return ['None']
        experiments = loaded_json['experiments']['experiment']
        experiments = self._any_has_any(keywords, experiments)
        experiments = [exp for exp in experiments if exp.has_key('experimenttype')]
        for i in experiments:
            print i['experimenttype'], experiment
        experiments = [exp for exp in experiments if len([extype for extype in experiment if extype in str(exp['experimenttype'])]) > 0]
        if len(experiments) == 0:
            experiments = ['None']
        return experiments

    def search(self, keywords=[], experiment=[]):
        ''' '''
        self.content = url.urlopen(self.query)
        self.content = self.content.read()

        self.content = self._parse_json(self.content, keywords, experiment)

    def get_results(self):
        ''' '''
        return self.content


