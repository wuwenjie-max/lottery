from django.http import JsonResponse

from utils.constant_utils import HttpMessage, HttpStatus


def response_data(data=[], msg=HttpMessage.Success.value, status=HttpStatus.Success.value):
    return JsonResponse({'msg': msg, 'status': status, 'data': data})

