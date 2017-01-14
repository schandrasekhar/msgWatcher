import pyinotify

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