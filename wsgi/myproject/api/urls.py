'''
Created on Aug 7, 2015

@author: luodichen
'''

from django.conf.urls import url

urlpatterns = [
    url(r'^test/$', 'api.views.test'),
    url(r'active/$', 'api.views.active'),
]
