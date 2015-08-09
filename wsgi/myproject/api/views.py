import json
import time
from models import DNSPodAccount
from models import User
from lib.response import JsonResponse
from lib.dnspod import DNSPod, DNSPodError

def active(request):
    response = {'code': 0, 'text': 'ok', 'ddns_update': False}
    
    token = request.REQUEST.get('token')
    if token is None:
        response['code'], response['text'] = -1, 'bad request'
        return JsonResponse(response)
    
    ip_addr = request.META['REMOTE_ADDR']
    response['ip_address'] = ip_addr
    
    try:
        user = User.objects.get(token=token)
        user.last_active_time = int(time.time())
        user.last_active_ip = ip_addr
        user.save()
        
        if user.sub_domain_id is not None and '' != user.sub_domain_id and \
                (ip_addr != user.ddns_ip or user.ddns_update_time is None or \
                 int(time.time()) - user.ddns_update_time > 600):
            response['ddns_update'] = True
            dnspod_account = DNSPodAccount.objects.get()
            dnspod = DNSPod(dnspod_account.username, dnspod_account.password)
            user.ddns_ip = dnspod.ddns(user.domain.domain_id, user.sub_domain_id, ip_addr)
            user.ddns_update_time = int(time.time())
            
            user.save()
    except User.DoesNotExist:
        response['code'], response['text'] = 1, 'token not exists' 
    except DNSPodError, e:
        response['code'] = 2
        response['text'] = str(e)
    
    return JsonResponse(response)

def dnspod_setup(request):
    ret = {'code': 0, 'text': 'ok'}
    
    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')
    
    if username is None or password is None:
        ret['code'] = -1
        ret['text'] = 'bad request'
        return JsonResponse(ret)
    
    account = None
    
    if DNSPodAccount.objects.count() == 0:
        account = DNSPodAccount()
    else:
        account = DNSPodAccount.objects.get()
    
    account.username = username
    account.password = password
    account.save()
        
    return JsonResponse(ret)


