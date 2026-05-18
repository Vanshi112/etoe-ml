import sys
from src.logger import logging


def error_message_d(error,error_detail:sys):
    _,_, exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occur [{0}] line number [{1}] msg [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message





