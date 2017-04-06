#this is need for the multi threaded use case
import Queue
import threading

logFilePath = './log.txt'

#dummy ajax call
def ajax(line):
    print line

#get lines from file
def getLines(filename):
    with open(logFilePath, 'r') as file:
        lines = file.readlines()
    return lines

#single threaded solution
def send(arr):
    for line in lines:
        ajax(line)

#single threaded use case
# lines = getLines(logFilePath)
# send(lines)

#worker function to trigger ajax function
def worker():
    while True:
        line = lines.get()
        if line is None:
            break
        #ajax(line)
        lines.task_done()

threads = []
threadCount = 1000

#initialize thread with the task
def initThreads(threadCount, workerFunc):
    for i in range(threadCount):
        t = threading.Thread(target=workerFunc)
        t.start()
        threads.append(t)

def getLines(filename):
    q = Queue.Queue()
    with open(logFilePath) as file:
        lines = file.readlines()
    for line in lines:
        q.put(line)
    return q

def cleanup(threads, threadCount, lines):
    for i in range(threadCount):
        lines.put(None)
    for thread in threads:
        thread.join()

#multi threaded use case
lines = getLines(logFilePath)
initThreads(threadCount, worker)

# block until all tasks are done
lines.join()

# stop workers
cleanup(threads, threadCount, lines)


