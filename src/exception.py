import sys

def error_message_detail(error , error_detail: sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format()
    file_name, exc_tb.tb_lineno,str(error)
    
    return file_name,exc_tb.tb_lineno,str(error)


class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_details = error_details

