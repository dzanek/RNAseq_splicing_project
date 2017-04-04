import urllib2 as url
import json
import sys


args = ['*seq']
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
        return self.content
class Array_express_results:
    ''' '''
    def __init__(self, content):
        ''' '''
        self.content = content

    def parse_content(self):
        ''' '''
        self.content = [i for i in self.content if 'tnf' in str(i) or 'interleukin' or 'tf6' in str(i)]
        self.content = [i for i in self.content if len([k for k in i['experimenttype'] if 'seq' in k and 'RNA' in k ]) > 0]
        for k in ['hepato', 'adipo', 'epiderm']:
            thisone = [v for v in self.content if k in str(v)]
            print len(thisone)
            for v in thisone:
                print v['accession']
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
    #results.print_ids()
if __name__ == '__main__':
    main()
