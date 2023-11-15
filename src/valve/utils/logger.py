import os
import sys
import time
import datetime
from clint.textui import puts_err, colored

available_colors = {'red', 'green', 'yellow', 'blue', 'black', 'magenta', 'cyan', 'white'}

def colorize(msg, color):
    function = getattr(colored, color)
    formatted_msg = function(msg)
    return formatted_msg

def debug(msg, color="yellow"):
    if "VALVE_DEBUG" in os.environ:
        logit(msg, color)

def logit(msg, color=None):
    """
    Logs a message with an optional color.

    :param msg: The message to be logged.
    :type msg: str
    :param color: The color to apply to the message (optional).
    :type color: str
    """
    ts = time.strftime("[ %Y-%m-%d %T ]", datetime.datetime.now().timetuple())
    fullmsg = "{} {}".format(ts, msg)
    formatted_msg = colorize(fullmsg, color) if color in available_colors else fullmsg
    puts_err(formatted_msg)
    sys.stdout.flush()
    sys.stderr.flush()
