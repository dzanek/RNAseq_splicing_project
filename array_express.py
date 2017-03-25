import urllib2 as url
import json
import sys


args = ['*seq','hepatocyte']
organism = 'mouse'

class Array_express_search:
    ''' '''
    def __init__(self):
        ''' '''
        self.base_query = 'https://www.ebi.ac.uk/arrayexpress/json/v3/experiments'

    def get_keywords(self):
        ''' '''

        self.query = self.base_query + '?keywords={}&organism={}'.format('+'.join(args), organism)

    def get_results(self):
        ''' '''
        print self.query
        self.content = url.urlopen(self.query)
        self.content = self.content.read()
        self.content = json.loads(self.content)
        self.content = self.content['experiments']['experiment']
        print 'I fount {} experiments'.format(len(self.content))

class Array_express_results:
    ''' '''
    def __init__(self, content):
        ''' '''
        self.content = content

    def parse_content(self):
        ''' '''
        self.content = [i for i in self.content if 'RNA' in i['text'] or 'hepatocyte' in i['text']]
        self.content = [i for i in self,content if len([k for k in i['experimenttype'] if 'seq' in k ]) > 0]
        print 'after refinement {}'.format(len(self.content))

    def print_ids(self):
        ''' '''
        for i in self.content:
            print i['accession']

def main():
    ''' '''
    search = Array_express_search()
    search.get_keywords()
    results = Array_express_results(search.get_results())
    results.parse_content()

if __name__ == '__main__':
    main()
