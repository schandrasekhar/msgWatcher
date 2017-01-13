#a wrapper for file system functionality
import os

class FS(object):
    """docstring for FS"""
    def __init__(self):
        super(FS, self).__init__()
    def getFiles(self, path):
        files = []
        if len(path) > 0:
            for (dirpath, dirnames, filenames) in os.walk(path):
                files.extend(dirpath + "/" + filenames)
                break
        return files
    def getAllFiles(self, path):
        files = []
        if len(path) > 0:
            for (dirpath, dirnames, filenames) in os.walk(path):
                files.extend(dirpath + "/" + filenames)
        return files
    def getDirs(self, path):
        dirs = []
        if len(path) > 0:
            for (dirpath, dirnames, filenames) in os.walk(path):
                dirs.extend(dirpath + "/" + dirnames)
                break
        return dirs
    def getAllDirs(self, path):
        dirs = []
        if len(path) > 0:
            for (dirpath, dirnames, filenames) in os.walk(path):
                dirs.extend(dirpath + "/" + dirnames)
        return dirs
    def getAllFilesDirs(path):
        arr = []
        if len(path) > 0:
            for (dirpath, dirnames, filenames) in os.walk(path):
                arr.extend(dirpath + "/" + filenames)
                arr.extend(dirpath + "/" + dirnames)
            return arr

fs = FS()

files = fs.getAllFiles("/Users/srigiriraju/Documents/my-github/msgWatcher/")
print(files)
