# Create on Aug. 2, 2015 Sun.
# Shows the compex output format in Python (Used in logging.py of XX-Net)

import os
import sys
import time
import threading

buffer = {} # id => line
buffer_size = 500
last_no = 0
buffer_lock = threading.Lock()

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

# Default value of level
level = INFO

# Defines function set_console_color()
err_color = None
warn_color = None
debug_color = None
reset_color = None
set_console_color = lambda x: None
if hasattr(sys.stderr, 'isatty') and sys.stderr.isatty():
    if os.name == 'nt':
        err_color = 0x04
        warn_color = 0x06
        debug_color = 0x002
        reset_color = 0x07

        import ctypes
        SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute
        GetStdHandle = ctypes.windll.kernel32.GetStdHandle
        set_console_color = lambda color: SetConsoleTextAttribute(GetStdHandle(-11), color)

    elif os.name == 'posix':
        err_color = '\033[31m'
        warn_color = '\033[33m'
        debug_color = '\033[32m'
        reset_color = '\033[0m'

        set_console_color = lambda color: sys.stderr.write(color)


# time: Sun Aug  2 13:38:17 2015 -> [4:-5] -> Aug  2 13:38:17
# level: DEBUG, WARNING, INFO, ERROR, CRITICAL
# fmt % args: '%(levelname)s - %(asctime)s %(message)s' % args
# kwargs is not used at all
def log(level, console_color, html_color, fmt, *args, **kwargs):
    global last_no, buffer_lock, buffer, buffer_size
    # The output str object
    string = '%s - [%s] %s\n' % (time.ctime()[4:-5], level, fmt % args)
    buffer_lock.acquire()
    try:
        set_console_color(console_color)
        sys.stderr.write(string) # outputs here
        set_console_color(reset_color)

        last_no += 1
        buffer[last_no] = string
        buffer_len = len(buffer)
        if buffer_len > buffer_size:
            del buffer[last_no - buffer_size]
    except Exception as e:
        string = '%s - [%s]LOG_EXCEPT: %s, Except:%s<br>' % (time.ctime()[4:-5], level, fmt % args, e)
        last_no += 1
        buffer[last_no] = string
        buffer_len = len(buffer)
        if buffer_len > buffer_size:
            del buffer[last_no - buffer_size]
    finally:
        buffer_lock.release()


def debug(fmt, *args, **kwargs):
    log('DEBUG', debug_color, '21610b', fmt, *args, **kwargs)


def info(fmt, *args, **kwargs):
    log('INFO', reset_color, '000000', fmt, *args)


def warning(fmt, *args, **kwargs):
    log('WARNING', warn_color, 'FF8000', fmt, *args, **kwargs)


def error(fmt, *args, **kwargs):
    log('ERROR', err_color, 'FE2E2E', fmt, *args, **kwargs)


def critical(fmt, *args, **kwargs):
    log('CRITICAL', err_color, 'D7DF01', fmt, *args, **kwargs)


# Run this in the OS console to show the colors
if __name__ == "__main__":
    command = "GET"
    host = "http://www.example.com"
    port = 8080
    debug('FWD %s %s:%d closed', command, host, port)
    
    a, b = 1, 2
    c = a + b
    info("%d + %d = %d", a, b, c)
    
    c = 10
    warning("%d + %d != %d", a, b, c)
    
    error("%s:%d is unreachable!", host, port)
    
    critical("%s:%d is down!", host, port)
