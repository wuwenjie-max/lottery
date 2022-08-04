from enum import Enum, unique

@unique
class HttpMessage(Enum):
    Success = 200
    Error = 500
    Redirection = 300

@unique
class HttpStatus(Enum):
    Success = 'success'
    Error = 'error'
    Redirection = 'redirection'