import json
import time
from models import DNSPodAccount
from models import User
from lib.response import JsonResponse

def active(request):
    response = {'code': 0, 'text': 'ok'}
    
    token = request.REQUEST.get('token')
    if token is None:
        response['code'], response['text'] = -1, 'bad request'
        return JsonResponse(response)
    
    ip_addr = request.META['REMOTE_ADDR']
    
    try:
        user = User.objects.get(token=token)
        user.last_active_time = int(time.time())
        user.last_active_ip = ip_addr
        user.save()
    except User.DoesNotExist:
        response['code'], response['text'] = 1, 'token not exists'
    
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


