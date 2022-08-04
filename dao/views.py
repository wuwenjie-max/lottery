import datetime

from .models import TwoColorBall, BigLotto
from utils.response_utils import response_data
from utils.decorator_utils import exception_handle
# Create your views here.

@exception_handle
def query_two_color_balls_by_day(request, day):
    '''args:
        request:
        day: YYYY-mm-DD
    '''
    instance = TwoColorBall.objects.filter(data_time__startswith=datetime.datetime.strptime(day[:10], '%Y-%m-%d').date())
    return response_data(str(instance))

@exception_handle
def query_big_lotto_by_day(request, day):
    instance = BigLotto.objects.get(data_time__startswith=datetime.datetime.strptime(day[:10], '%Y-%m-%d').date())
    return response_data(str(instance))

@exception_handle
def query_two_color_balls_by_latest_number(request, number=1):
    if number > 0:
        instances = TwoColorBall.objects.order_by('-data_time')[:number]
    else:
        raise ValueError('number must greater than 0')
    return response_data({'latest': number, 'result': [str(i) for i in instances]})

@exception_handle
def query_big_lotto_by_latest_number(request, number=1):
    if number > 0:
        instances = BigLotto.objects.order_by('-data_time')[:number]
    else:
        raise ValueError('number must greater than 0')
    return response_data({'latest': number, 'result': [str(i) for i in instances]})