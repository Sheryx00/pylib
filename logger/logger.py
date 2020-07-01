"""
##################################

Logger - log quicky to the output!

VERSION: 1.0
REPOSITORY: https://github.com/schrocpgerardo/Pocket-Console-Log-for-python

##################################

        Welcome To Logger.

        Logger was created by the urgent of a simply, lightweight library which could
        be copy and used just like a print function, but with colors and log level output.
"""

import sys
from pylib.colors import colors as c

#   COLORS COOKWORK
message     = c.message
colors      = c.colors

bold        = colors.bold
reset_color = colors.reset
white       = colors.lightgrey
lightcyan   = colors.lightcyan
green       = colors.green
pink        = colors.pink + colors.bold
orange      = colors.orange
red         = colors.red

DEBUG       = white+"["+lightcyan+bold+"DEBUG"+reset_color+white+"]"+white+reset_color+" "
INFO        = white+"["+white+bold+"INFO"+reset_color+white+"]"+white+reset_color+" "
RUN         = white+"["+green+bold+"RUN"+reset_color+white+"]"+white+reset_color+" "
AST         = white+"["+pink+"*"+reset_color+white+"]"+white+reset_color+" "
WARNING     = white+"["+orange+bold+"WARNING"+reset_color+white+"]"+white+reset_color+" "
ERROR       = white+"["+red+bold+"ERRRO"+reset_color+white+"]"+white+reset_color+" "
CRITICAL    = white+"["+red+bold+"CRITICAL"+reset_color+white+"]"+white+reset_color+" "

# LOGGING
set_level = 'info' # this is the default level
debug_index = ["debug", "info", "success", "warning", "error", "critical"]

logging = {
            # '' :        ['',''],
            'debug':    [DEBUG, lightcyan],
            'info':     [INFO, white],
            'ast':      [AST, pink],
            'run':      [RUN, green],
            'warning':  [WARNING, orange],
            'error':    [ERROR, red],
            'critical': [CRITICAL, red],
            }


def set_new_level(level):
    """
        This function set a new level for the logger.
    """
    try:
        if level in debug_index:
            global set_level
            set_level = level
            print("The level of logger has changed to: %s " % (bold + set_level + reset_color))
        else:
            print('Must choice one of this list: %s' % debug_index)
    except Exception as e:
        print(e)

def log(level, msg=None, clr='reset', *args, **kwargs):
    """
        It work over message() of 'colors' module, so if you only need to print
        the message, with colors but not a log level, please check 'colors' module.

        Its pretty easy to use logger, try this example:
            import logger as log
            log('info', "this is your message")
            # This line will print "this is your message" with the assigned 'info' log level.

            'info' is the default level, but can be change using the same log(), just
            write which level you want to set without message at all:
                # This line will set 'debug' as the new log level. Any new message with
                # a level highter than 'debug' will be print, and ignored if not.

                import logger as log
                log('debug')

            Thats all. The rest of this function() is just like color.message(), so you
            could do something mixed like:
            log('info', "this message will be have a colored word", 'blue', word='colored')
"""
    try:
        if not msg:
            return set_new_level(level)
        else:
            if debug_index.index(level) >= debug_index.index(set_level):
                clr = clr if clr != 'reset' else logging[level][0]
                msg = message(msg, clr=clr, **kwargs)
    except Exception as e:
        print(str(e))
