from functools import wraps
import loguru

from utils.response_utils import response_data, HttpMessage, HttpStatus

def exception_handle(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            loguru.logger.exception(e)
            return response_data(data=str(e), msg=HttpMessage.Error.value, status=HttpStatus.Error.value)
        return result
    return inner