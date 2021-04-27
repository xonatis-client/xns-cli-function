from typing import Optional
from models.token import Token
from models.app_description import AppDescription
from models.function import Function

class AppFunction(Function):
    def process(self, app_description: AppDescription, token: Optional[Token], method, url_args, get_args, data_args):
        return {
            'success' : True
        }