import valve.utils.logger as log

def hello(debug):
    if debug:
        log.logit("Hello There! (with debug flag)", color="yellow")
    else:
        log.logit("Hello There!")
