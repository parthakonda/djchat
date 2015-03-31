from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import View
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import SELF
import json

def chat(request):
    return render_to_response("chat.html", {}, context_instance=RequestContext(request))

def home(request):
    return render_to_response("home.html", {}, context_instance=RequestContext(request))    

def publishMessage(request):
    message = "dummy"
    toUser = request.GET['username']
    if 'message' in request.GET:
        message = request.GET['message']
    redis_publisher = RedisPublisher(facility='notifications', users=[request.user.username, toUser])
    data = {
        'sender':request.user.username,
        'message':message
    }
    message = RedisMessage(json.dumps(data))
    redis_publisher.publish_message(message)
    return HttpResponse("Published")