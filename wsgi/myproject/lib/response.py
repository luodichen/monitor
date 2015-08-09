'''
Created on Aug 8, 2015

@author: luodichen
'''
import json
from django.http.response import HttpResponse

class JsonResponse(HttpResponse):
    def __init__(self, json_object):
        HttpResponse.__init__(self, json.dumps(json_object), 
                              content_type='application/json')
