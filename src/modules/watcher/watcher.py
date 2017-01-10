import pyinotify

DIR_TO_WATCH=/tmp

wm = pyinotify.WatchManager()

dir_events = pyinotify.IN_CREATE

class EventHandler(pyinotify.ProcessEvent):
    """docstring for EventHandler"""
    def __init__(self, arg):
        super(EventHandler, self).__init__()
        self.arg = arg

    def process_IN_CREATE(self, event):
        print(File %s was deleted % event.pathname)

event_handler = EventHandler()
notifier = pyinotify.Notifier(wm, event_handler)

wm.add_watch(DIR_TO_WATCH, dir_events)

notifier.loop()