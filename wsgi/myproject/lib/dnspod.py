'''
Created on Aug 9, 2015

@author: luodichen
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import urllib
import urllib2

class DNSPodError(Exception):
    def __init__(self, value):
            self.value = value
    def __str__(self):
        return repr(self.value)

class DomainRecord(object):
    
    def __init__(self, data):
        if '1' != data['status']['code']:
            raise DNSPodError(data['status']['message'])
        
        record = data['record']
        
        self.data = data
        self.id = record['id']
        self.domain_id = record['domain_id']
        self.sub_domain = record['sub_domain']
        self.record_type = record['record_type']
        self.record_line = record['record_line']
        self.value = record['value']
        self.mx = record['mx']
        self.ttl = record['ttl']
        self.enabled = record['enabled']
        self.monitor_status = record['monitor_status']
        self.remark = record['remark']
        self.updated = record['updated_on']  
    
    def __str__(self):
        return repr(self.data)

class DnsPod(object):
    URL                 = 'https://dnsapi.cn'
    RECORD_INFO         = URL + '/Record.Info'
    DDNS                = URL + '/Record.Ddns'
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def com_request(self):
        return { 'login_email': self.username, 
                 'login_password': self.password,
                 'format': 'json',
        }
        
    def request(self, url, req):
        request = urllib2.Request(url, data=urllib.urlencode(req))
        return json.loads(urllib2.urlopen(request).read())
        
    def record_info(self, domain_id, record_id):
        request = self.com_request()
        request['domain_id'] = domain_id
        request['record_id'] = record_id
        
        return DomainRecord(self.request(self.RECORD_INFO, request))

    def ddns(self, domain_id, record_id, ipaddress):
        record = self.record_info(domain_id, record_id)
        if ipaddress == record.value:
            return ipaddress
        
        request = self.com_request()
        request['domain_id'] = domain_id
        request['record_id'] = record_id
        request['sub_domain'] = record.sub_domain
        request['record_line'] = record.record_line
        request['value'] = ipaddress
        
        response = self.request(self.DDNS, request)
        if '1' != response['status']['code']:
            raise DNSPodError(response['status']['message'])
        
        return response['record']['value']
