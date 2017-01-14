# Example: loops monitoring events forever.
#
import pyinotify


wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# # process events).
# notifier = pyinotify.Notifier(wm)
# # Add a new watch on /tmp for ALL_EVENTS.
# wm.add_watch('/tmp', pyinotify.ALL_EVENTS)
# # Loop forever and handle events.
# def callback(obj):
#     print(obj)


# notifier.loop(callback=callback)


# steps for this feature
#1. loop through the directory and get all the file descriptors
#2. add watcher for each file (event name IN_MODIFY)
#3. print on event (for now)

#what do i want
# a higher level of instance to which i pass an array of filepaths (or) dirpaths and
# the events for which i will want to do some functionality, in terms of (js) execute a
# callback

class Watcher(object):
    """docstring for Watcher"""
    def __init__(self, path, event):
        super(Watcher, self).__init__()
        self._path = path
        self._event = event
    def _bind(self):
        self._wm.add_watch(self._path, self._event)
    def getNotifier(self):
        wm = pyinotify.WatchManager()
        self._wm = wm
        self._notifier = pyinotify.Notifier(self._wm)
        self._bind()
        return self._notifier

class Logger(object):
    """docstring for Logger"""
    def __init__(self):
        super(Logger, self).__init__()
        self.arg = arg
    def onLog(self, eventObj):
        print(eventObj)


path = "/tmp"
event = pyinotify.IN_MODIFY
watcher = Watcher(path, event)
notifier = watcher.getNotifier()
logger = Logger()
notifier.loop(callback=logger.onLog)

