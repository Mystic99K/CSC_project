import time


def error_handle(error_code):
    error_desc = open('errors.txt', 'r')  # Opening existing list of errors

    EL = error_desc.readlines()
    for EC in EL:
        if str(error_code) == EC[:3]:  # Splicing Error code to Match Error code with existing errors
            ED = EC[4:-2:] + "'"  # Splicing Error code to only get Error detail
            break
    else:
        ED = 'Unknown Error'

    error_desc.close()

    # Error logging part
    log_file = open('Error_Log.txt', 'a')  # Opening existing log file

    C_Time = time.localtime()[::]  # Getting Current time

    log_write = C_Time[1], '/', C_Time[2], '/', C_Time[0], ' ', C_Time[3], ':', C_Time[4], ':', C_Time[
        5], '\t', 'ERROR:', error_code, ' ', '-', ' ', ED  # Formatting Error Log
    log_line = ''

    for log_word in log_write:  # converting tuple to string without changing format
        log_line = log_line + str(log_word)

    log_file.write(log_line + '\n')  # Writing into Log File
    log_file.close()
