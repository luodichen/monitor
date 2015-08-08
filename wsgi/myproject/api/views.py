import json
import time
from models import User
from response import JsonResponse

def active(request):
    response = {'code': 0, 'text': 'ok'}
    token = None
    ip_addr = None
    
    try:
        quest_data = json.loads(request.REQUEST.get('q'))
        token = quest_data['token']
        ip_addr = request.META['REMOTE_ADDR']
    except:
        response['code'], response['text'] = -1, 'bad request'
        return JsonResponse(response)
    
    try:
        user = User.objects.get(token=token)
        user.last_active_time = int(time.time())
        user.last_active_ip = ip_addr
        user.save()
    except User.DoesNotExist:
        response['code'], response['text'] = 1, 'token not exists'
    
    return JsonResponse(response)

