
"""

Colors

##################################

Colors - for your cli!

VERSION: 1.0
REPOSITORY: https://github.com/schrottgerardo/pylib

##################################
"""

class colors:
    """
        This is your colors palette inspired in Gi Jack works, at link below.
        You can add or remove any you want. Need to find more? check this:
        https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
    """
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'

    def set(self, color):
        return getattr(self, color)

def bold(msg, word, clr):
    """
        When 'word' is used, it print that word with bold and color style.
        If clr is used too, then it is used too (clr is 'reset' by default
        from message)

        Most of the time you will prefer use messsage() with keyword 'word'
        instead of call bold() directly.
    """
    clr = 'lightgrey' if clr == 'reset' else clr
    new_bold = str(colors.bold + colors().set(clr) + word + colors.reset)
    msg = msg.replace(word, new_bold)
    return msg

def message(msg, clr="reset", **kwargs):
    """
        This function can be ussed just like the standard print(),
        but it add the 'clr' argument, which will use colors if any color
        is passed. 'clr' must be exist in class colors().

        keyword 'end' of print() works just like usual here.

        examples:
            message("this is your message")
            message("this is your message", 'orange')
            message("this is your message", 'orange', end='')
    """
    color = colors()
    try:
        color = color.set(clr)
        msg = bold(msg, kwargs.get('word'), clr) if 'word' in kwargs else color+msg+colors.reset
        if 'end' in kwargs: print(str(msg), end=kwargs.get('end'))
        else: print(msg)
    except Exception as e:
        print("(weird) error in colors. Try to debug it or report the issue")
        print(e)
