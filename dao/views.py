from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

from .models import TwoColorBall, BigLotto
# Create your views here.

def query_two_color_balls_by_day(request, day):
    '''args:
        request:
        day: YYYY-mm-DD HH:MM:SS
    '''
    instance = TwoColorBall.objects.get(data_time=datetime.datetime.strptime(day[:10], 'YYYY-mm-DD'))
    return HttpResponse(str(instance))

def query_big_lotto_by_day(request, day):
    instance = BigLotto.objects.get(data_time=datetime.datetime.strptime(day[:10], 'YYYY-mm-DD'))
    return HttpResponse(str(instance))

def query_two_color_balls_by_latest_number(request, number=1):
    if number > 0:
        instances = TwoColorBall.objects.order_by('-data_time')[:number]
    else:
        raise ValueError('number must greater than 0')
    return HttpResponse('latest {number}:\n'.format('/n'.split([str(i) for i in instances])))

def query_big_lotto_by_latest_number(request, number=1):
    if number > 0:
        instances = BigLotto.objects.order_by('-data_time')[:number]
    else:
        raise ValueError('number must greater than 0')
    return HttpResponse('latest {number}:\n'.format('/n'.split([str(i) for i in instances])))