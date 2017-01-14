#Logger will get invoked on fs event, it will
#1. get the file name for the event

class LogManager(object):
    """docstring for LogManager"""
    def __init__(self):
        super(LogManager, self).__init__()
    def onLog(self, eventObj):
        print(eventObj)