#path = "/tmp"
# event = pyinotify.IN_MODIFY
# watcher = Watcher(path, event)
# notifier = watcher.getNotifier()
# logger = LogManager()
# notifier.loop(callback=logger.onLog)


#usecase for single file
#1. Initial Setup
    #1. config setup
        #1. create a directory for saving line numbers sent for each log file if it does not exist
            #(the structure used here is a hash map with the file path as the key and line number as the value)
            #the line number counts will be kept in ram and flushed to hard drive once in a while to prevent i/o
            #overhead for the application machine 
        #2. setup kafka publishers and proceed if and only if this is a SUCCESS
        #3. setup file descriptors for each of the log files in the given directory
    #2. get line numbers of each file from that file (or) set all to zero if no file exists
    #3. setup listening to the log directory for IN_MODIFY events and start queueing up file events
    #4. check each log file to see if any previous data needs to be sent (based on the line number)
        #1. if data needs to be sent, get data from the file and send to kafka publisher
    #5. once #4 is done, start popping event objects from the queue for processing
        #1. get the line number from the previous steps and check if data really exists using the respective
            #file descriptor
                #1. if data exists send to kafka publisher
                    #1. kafka on success, will send update to the process managing the line number count of
                        #that file
#1.listen for IN_MODIFY events on given directory
#2.put all events in queue
#3.pop from queue and give event object to msgGetter


#functionality to get a line from file
path = "/tmp/trial"
with open(path) as f:
    content = f.readlines()
print(content)
